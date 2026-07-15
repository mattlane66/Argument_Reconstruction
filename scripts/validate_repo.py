#!/usr/bin/env python3
"""Validate the Argument Reconstruction repository without third-party packages."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LEGACY_SKILL_DIRS = {
    "argument_reconstruction_full",
    "reconstruct_charity",
    "reconstruct_conclusion",
    "reconstruct_premises",
    "reconstruct_hidden_bridge",
    "reconstruct_linkage",
    "reconstruct_removal_test",
    "reconstruct_counterexample",
    "reconstruct_fallacy_check",
    "reconstruct_reality_check",
}


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid or unreadable JSON: {exc}")
        return None


def validate_skill(path: Path, errors: list[str]) -> None:
    relative = path.relative_to(ROOT)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{relative}: unreadable: {exc}")
        return

    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append(f"{relative}: missing opening YAML delimiter")
        return

    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"{relative}: missing closing YAML delimiter")
        return

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        if not separator or not key.strip() or not value.strip():
            errors.append(f"{relative}: malformed frontmatter line: {line!r}")
            continue
        fields[key.strip()] = value.strip()

    if set(fields) != {"name", "description"}:
        errors.append(f"{relative}: frontmatter must contain only name and description")
        return

    name = fields["name"].strip('"\'')
    if not NAME_RE.fullmatch(name):
        errors.append(f"{relative}: name must be lowercase hyphen-case")
    if path.parent.name != name:
        errors.append(f"{relative}: folder name must match skill name {name!r}")

    description = fields["description"]
    if not (description.startswith('"') and description.endswith('"')):
        errors.append(f"{relative}: quote the description to keep YAML unambiguous")
    else:
        try:
            if not json.loads(description).strip():
                errors.append(f"{relative}: description must not be empty")
        except json.JSONDecodeError as exc:
            errors.append(f"{relative}: description is not a valid quoted string: {exc}")

    if len(lines) > 500:
        errors.append(f"{relative}: skill body exceeds 500 lines")
    if len(text.split()) > 5000:
        errors.append(f"{relative}: skill exceeds 5,000 words")


def main() -> int:
    errors: list[str] = []

    manifest_path = ROOT / "manifest.json"
    manifest = load_json(manifest_path, errors)
    if not isinstance(manifest, dict):
        manifest = {}

    if manifest.get("version") != "2.0.0":
        errors.append("manifest.json: expected version 2.0.0")

    declared_paths: list[str] = []
    for key in ("skills", "skill_resources", "examples", "tests"):
        value = manifest.get(key, [])
        if not isinstance(value, list):
            errors.append(f"manifest.json: {key} must be a list")
            continue
        declared_paths.extend(item for item in value if isinstance(item, str))

    for key in ("custom_gpt_instruction_block", "knowledge_sources", "validation"):
        value = manifest.get(key)
        if isinstance(value, str):
            declared_paths.append(value)
        else:
            errors.append(f"manifest.json: {key} must be a path string")

    for declared in declared_paths:
        if not (ROOT / declared).is_file():
            errors.append(f"manifest.json: declared path does not exist: {declared}")

    skills = manifest.get("skills", [])
    if skills != ["argument-reconstruction/SKILL.md"]:
        errors.append("manifest.json: expected one canonical argument-reconstruction skill")
    for skill in skills if isinstance(skills, list) else []:
        if isinstance(skill, str) and (ROOT / skill).is_file():
            validate_skill(ROOT / skill, errors)

    for legacy in sorted(LEGACY_SKILL_DIRS):
        if (ROOT / legacy / "SKILL.md").exists():
            errors.append(f"legacy skill still exists: {legacy}/SKILL.md")

    instructions_path = ROOT / "custom_gpt_instruction_block.md"
    if instructions_path.is_file():
        character_count = len(instructions_path.read_text(encoding="utf-8"))
        if character_count > 8000:
            errors.append(
                "custom_gpt_instruction_block.md: "
                f"{character_count:,} characters exceeds the 8,000-character limit"
            )

    agents_path = ROOT / "argument-reconstruction/agents/openai.yaml"
    if agents_path.is_file():
        agents_text = agents_path.read_text(encoding="utf-8")
        short_match = re.search(r'^\s+short_description: "([^"]+)"$', agents_text, re.MULTILINE)
        prompt_match = re.search(r'^\s+default_prompt: "([^"]+)"$', agents_text, re.MULTILINE)
        if not short_match or not 25 <= len(short_match.group(1)) <= 64:
            errors.append("agents/openai.yaml: short_description must contain 25-64 characters")
        if not prompt_match or "$argument-reconstruction" not in prompt_match.group(1):
            errors.append("agents/openai.yaml: default_prompt must mention $argument-reconstruction")

    knowledge = load_json(ROOT / "knowledge_sources.json", errors)
    if isinstance(knowledge, dict):
        if not knowledge.get("sources"):
            errors.append("knowledge_sources.json: document at least one methodology source")
        attachments = knowledge.get("custom_gpt_knowledge_attachments")
        if not isinstance(attachments, dict) or "documented_attachments" not in attachments:
            errors.append("knowledge_sources.json: document Custom GPT attachment status")

    cases_doc = load_json(ROOT / "tests/cases.json", errors)
    if isinstance(cases_doc, dict):
        cases = cases_doc.get("cases")
        if not isinstance(cases, list) or len(cases) < 10:
            errors.append("tests/cases.json: include at least 10 contract cases")
        else:
            ids: list[str] = []
            for index, case in enumerate(cases, start=1):
                if not isinstance(case, dict):
                    errors.append(f"tests/cases.json: case {index} must be an object")
                    continue
                case_id = case.get("id")
                if not isinstance(case_id, str) or not NAME_RE.fullmatch(case_id):
                    errors.append(f"tests/cases.json: case {index} has an invalid id")
                else:
                    ids.append(case_id)
                if not isinstance(case.get("input"), str) or not case["input"].strip():
                    errors.append(f"tests/cases.json: {case_id or index} needs input text")
                for key in ("required_moves", "prohibited_moves"):
                    value = case.get(key)
                    if not isinstance(value, list) or not value or not all(
                        isinstance(item, str) and item.strip() for item in value
                    ):
                        errors.append(f"tests/cases.json: {case_id or index} needs {key}")
            if len(ids) != len(set(ids)):
                errors.append("tests/cases.json: case ids must be unique")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
