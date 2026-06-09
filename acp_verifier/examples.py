from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .checks import CheckResult, check_packet
from .schemas import validate_packet_schema


REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = REPO_ROOT / "examples"


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    if not isinstance(data, dict):
        raise ValueError(f"expected YAML object in {path}")
    return data


def example_paths(path: str | None = None) -> list[Path]:
    if path:
        selected = Path(path)
        if selected.is_dir():
            return sorted(selected.glob("*.yaml")) + sorted(selected.glob("*.yml"))
        return [selected]
    return sorted(EXAMPLES_DIR.glob("*.yaml")) + sorted(EXAMPLES_DIR.glob("*.yml"))


def verify_packet_file(path: Path) -> list[CheckResult]:
    packet = load_yaml(path)
    checks: list[CheckResult] = []

    schema_errors = validate_packet_schema(packet)
    if schema_errors:
        for index, error in enumerate(schema_errors, start=1):
            checks.append(CheckResult(f"ACP-SCHEMA-{index:03d}", "fail", error))
    else:
        checks.append(CheckResult("ACP-SCHEMA", "pass", f"{path} matches context packet schema"))

    checks.extend(check_packet(packet))
    return checks


def verify_examples(path: str | None = None) -> list[CheckResult]:
    checks: list[CheckResult] = []
    paths = example_paths(path)

    if not paths:
        return [CheckResult("ACP-EXAMPLES", "fail", "no example files found")]

    for example_path in paths:
        try:
            checks.append(CheckResult("ACP-EXAMPLE-LOAD", "pass", f"loaded {example_path}"))
            checks.extend(verify_packet_file(example_path))
        except Exception as exc:
            checks.append(CheckResult("ACP-EXAMPLE-LOAD", "fail", f"{example_path}: {exc}"))

    return checks
