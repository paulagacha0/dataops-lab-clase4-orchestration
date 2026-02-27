import csv


class DataEnricher:
    def __init__(self, config: dict):
        self.catalog_path = config["catalog_path"]

    def enrich(self, processed_data):
        catalog = {}
        with open(self.catalog_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                catalog[row["product_id"]] = row

        enriched = []
        for r in processed_data:
            pid = r.get("product_id")
            info = catalog.get(pid, {})
            r2 = dict(r)
            r2["product_name"] = info.get("product_name", "UNKNOWN")
            r2["category"] = info.get("category", "UNKNOWN")
            enriched.append(r2)

        return {"enriched_data": enriched}