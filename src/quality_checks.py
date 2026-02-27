from datetime import datetime, timezone


class QualityChecker:
    def __init__(self, config: dict):
        self.checks = config.get("checks", [])

    def check_quality(self, data):
        issues = []

        # ---- Completeness threshold ----
        threshold = 0.95
        for c in self.checks:
            if "completeness_threshold" in c:
                threshold = float(c.split(":")[1].strip())

        ok = 0
        for r in data:
            # Consideramos "completo" si tiene total y product_name no es UNKNOWN
            if r.get("total") is not None and r.get("product_name") != "UNKNOWN":
                ok += 1

        completeness = ok / max(len(data), 1)
        if completeness < threshold:
            issues.append(f"Completitud baja: {completeness:.2f} < {threshold}")

        # ---- Freshness (mínimo: que exista sale_timestamp) ----
        for r in data:
            if not r.get("sale_timestamp"):
                issues.append("Frescura: sale_timestamp faltante")
                break

        passed = len(issues) == 0
        return {
            "passed": passed,
            "issues": issues,
            "checked_at": datetime.now(timezone.utc).isoformat(),
        }