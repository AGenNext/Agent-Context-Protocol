from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = REPO_ROOT / "schemas"


def load_schema(name: str) -> dict[str, Any]:
    path = SCHEMA_DIR / name
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def validate_with_schema(instance: dict[str, Any], schema_name: str) -> list[str]:
    schema = load_schema(schema_name)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    return [f"{list(error.path)}: {error.message}" for error in errors]


def validate_packet_schema(packet: dict[str, Any]) -> list[str]:
    return validate_with_schema(packet, "context-packet.schema.json")
