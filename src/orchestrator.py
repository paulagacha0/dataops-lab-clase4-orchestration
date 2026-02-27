import yaml
import logging
import json
import os
from datetime import datetime

from src.data_validation import DataValidator
from src.data_processing import DataProcessor
from src.data_enrichment import DataEnricher
from src.quality_checks import QualityChecker


class PipelineOrchestrator:
    def __init__(self, config_path="config/pipeline_config.yaml"):
        self.config = self.load_config(config_path)
        self.setup_logging()

    def load_config(self, config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def setup_logging(self):
        os.makedirs("logs", exist_ok=True)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("logs/pipeline_execution.log"),
                logging.StreamHandler()
            ],
        )
        self.logger = logging.getLogger(__name__)

    def execute_pipeline(self):
        execution_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.logger.info(f"Iniciando ejecución del pipeline: {execution_id}")

        try:
            self.logger.info("Ejecutando validación de datos...")
            validator = DataValidator(self.config["validation"])
            validation_result = validator.validate()
            if not validation_result["success"]:
                raise Exception(f"Validación fallida: {validation_result['errors']}")

            self.logger.info("Ejecutando procesamiento de datos...")
            processor = DataProcessor(self.config["processing"])
            processing_result = processor.process()

            self.logger.info("Ejecutando enriquecimiento de datos...")
            enricher = DataEnricher(self.config["enrichment"])
            enrichment_result = enricher.enrich(processing_result["processed_data"])

            self.logger.info("Ejecutando validación de calidad...")
            quality_checker = QualityChecker(self.config["quality"])
            quality_result = quality_checker.check_quality(enrichment_result["enriched_data"])
            if not quality_result["passed"]:
                raise Exception(f"Validación de calidad fallida: {quality_result['issues']}")

            self.logger.info("Generando reportes...")
            self.generate_reports(enrichment_result["enriched_data"], execution_id)

            self.logger.info(f"Pipeline completado exitosamente: {execution_id}")
            return {
                "success": True,
                "execution_id": execution_id,
                "records_processed": processing_result["record_count"],
            }

        except Exception as e:
            self.logger.error(f"Error en el pipeline: {str(e)}")
            self.send_alert(f"Pipeline falló: {str(e)}")
            return {"success": False, "error": str(e)}

    def generate_reports(self, data, execution_id):
        os.makedirs("data/outputs", exist_ok=True)
        report = {
            "execution_id": execution_id,
            "timestamp": datetime.now().isoformat(),
            "records_processed": len(data),
            "pipeline_version": self.config.get("version"),
        }
        with open(f"data/outputs/report_{execution_id}.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

    def send_alert(self, message):
        self.logger.info(f"ALERTA: {message}")


if __name__ == "__main__":
    orchestrator = PipelineOrchestrator("config/pipeline_config.yaml")
    result = orchestrator.execute_pipeline()
    print(result)