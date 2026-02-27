import json
import os


class DataValidator:
    def __init__(self, config: dict):
        self.schema_path = config["schema_path"]
        self.required_files = config.get("required_files", [])

    def validate(self):
        errors = []

        if not os.path.exists(self.schema_path):
            errors.append(f"Schema no encontrado: {self.schema_path}")
            return {"success": False, "errors": errors}

        with open(self.schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)

        required_cols = schema.get("required_columns", [])
        if not required_cols:
            errors.append("Schema inválido: required_columns vacío")

        file_map = {
            "sales_data.csv": "data/raw/sales_data.csv",
            "product_catalog.csv": "data/reference/product_catalog.csv",
        }

        for fname in self.required_files:
            path = file_map.get(fname, fname)
            if not os.path.exists(path):
                errors.append(f"Archivo requerido no encontrado: {path}")

        if errors:
            return {"success": False, "errors": errors}

        return {"success": True, "errors": []}