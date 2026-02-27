from src.orchestrator import PipelineOrchestrator


def test_integration_pipeline_runs():
    orchestrator = PipelineOrchestrator("config/pipeline_config.yaml")
    result = orchestrator.execute_pipeline()
    assert result["success"] is True, result
