import yaml

REQUIRED_TOP_KEYS = ["version", "validation", "processing", "enrichment", "quality"]

def main():
    with open("config/pipeline_config.yaml", "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    missing = [k for k in REQUIRED_TOP_KEYS if k not in cfg]
    if missing:
        raise SystemExit(f"Config inválida. Faltan keys: {missing}")

    print("Config OK")

if __name__ == "__main__":
    main()