from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class CheckResult:
    id: str
    status: str
    reason: str

    def as_dict(self) -> dict[str, str]:
        return {"id": self.id, "status": self.status, "reason": self.reason}


def _parse_dt(value: str) -> datetime | None:
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        return datetime.fromisoformat(value)
    except Exception:
        return None


def check_packet(packet: dict[str, Any]) -> list[CheckResult]:
    checks: list[CheckResult] = []

    def require(path: str, value: Any) -> None:
        if value in (None, ""):
            checks.append(CheckResult(path, "fail", f"missing required field: {path}"))
        else:
            checks.append(CheckResult(path, "pass", f"present: {path}"))

    require("packet_type", packet.get("packet_type"))
    if packet.get("packet_type") != "signed_jit_context_packet":
        checks.append(CheckResult("ACP-PACKET-TYPE", "fail", "packet_type must be signed_jit_context_packet"))
    else:
        checks.append(CheckResult("ACP-PACKET-TYPE", "pass", "packet type is valid"))

    for field in ["context_id", "actor", "agent", "tenant", "contract", "intent", "action", "target"]:
        require(field, packet.get(field))

    proof = packet.get("proof") or {}
    for field in ["signature", "signed_by", "signed_at", "policy_hash", "contract_hash"]:
        require(f"proof.{field}", proof.get(field))

    time_window = packet.get("time_window") or {}
    require("time_window.start", time_window.get("start"))
    require("time_window.end", time_window.get("end"))

    start = _parse_dt(time_window.get("start", "")) if isinstance(time_window.get("start"), str) else None
    end = _parse_dt(time_window.get("end", "")) if isinstance(time_window.get("end"), str) else None

    if start and end and end > start:
        checks.append(CheckResult("ACP-EXPIRY-FINITE", "pass", "time window is finite and ordered"))
    else:
        checks.append(CheckResult("ACP-EXPIRY-FINITE", "fail", "time_window.end must be after time_window.start"))

    for field in [
        "allowed_actions",
        "denied_actions",
        "allowed_tools",
        "denied_tools",
        "allowed_data",
        "denied_data",
        "redacted_data",
        "allowed_memory",
        "denied_memory",
        "obligations",
    ]:
        if isinstance(packet.get(field), list):
            checks.append(CheckResult(f"ACP-SCOPE-{field}", "pass", f"{field} is an array"))
        else:
            checks.append(CheckResult(f"ACP-SCOPE-{field}", "fail", f"{field} must be an array"))

    if packet.get("decision", {}).get("result") == "deny":
        checks.append(CheckResult("ACP-DENY-EXAMPLE", "pass", "denied packet contains denial decision"))

    evaluation = packet.get("evaluation", {})
    if evaluation.get("result") == "deny" and evaluation.get("reason") == "context_expired":
        now = _parse_dt(evaluation.get("now", "")) if isinstance(evaluation.get("now"), str) else None
        if now and end and now > end:
            checks.append(CheckResult("ACP-EXPIRED-EXAMPLE", "pass", "expired example is correctly denied"))
        else:
            checks.append(CheckResult("ACP-EXPIRED-EXAMPLE", "fail", "expired example denial does not match time window"))

    if "federation" in packet:
        federation = packet.get("federation") or {}
        for field in ["federation_id", "source_tenant", "destination_tenant", "federation_policy", "federation_contract"]:
            require(f"federation.{field}", federation.get(field))
        if "provenance" in packet:
            checks.append(CheckResult("ACP-FEDERATION-PROVENANCE", "pass", "federated packet includes provenance"))
        else:
            checks.append(CheckResult("ACP-FEDERATION-PROVENANCE", "fail", "federated packet must include provenance"))

    return checks


def summarize(checks: list[CheckResult]) -> dict[str, Any]:
    failed = [check for check in checks if check.status == "fail"]
    return {
        "result": "fail" if failed else "pass",
        "checks": [check.as_dict() for check in checks],
    }
