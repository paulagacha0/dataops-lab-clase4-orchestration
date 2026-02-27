import csv
import os


class DataProcessor:
    def __init__(self, config: dict):
        self.output_path = config["output_path"]
        self.steps = config.get("steps", [])

    def process(self):
        os.makedirs(self.output_path, exist_ok=True)

        input_path = "data/raw/sales_data.csv"
        processed = []

        with open(input_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                processed.append(row)

        if "clean_duplicates" in self.steps:
            seen = set()
            dedup = []
            for r in processed:
                key = (r.get("sale_id"), r.get("product_id"), r.get("sale_timestamp"))
                if key not in seen:
                    seen.add(key)
                    dedup.append(r)
            processed = dedup

        if "handle_missing_values" in self.steps:
            for r in processed:
                if r.get("quantity") in (None, "", " "):
                    r["quantity"] = "0"

        if "calculate_totals" in self.steps:
            for r in processed:
                q = float(r.get("quantity", 0) or 0)
                p = float(r.get("unit_price", 0) or 0)
                r["total"] = str(q * p)

        return {"processed_data": processed, "record_count": len(processed)}