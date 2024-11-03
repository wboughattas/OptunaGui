from fastapi import APIRouter
from server.schemas.experiments import ExperimentConfig, FeatureSelectionConfig, ModelPresetsResponse

router = APIRouter()


@router.post("/init", response_model=dict)
async def initialize_experiment(config: ExperimentConfig):
    """
    Initialize a new experiment with configurations such as model type, hyperparameter ranges, dataset selection,
    and splitting method.
    """
    return {"status": "success"}


@router.post("/{experiment_id}/features", response_model=dict)
async def configure_features(experiment_id: str, features: FeatureSelectionConfig):
    """
    Configure feature selection and engineering options for a specific experiment.
    """
    return {"status": "success"}


@router.get("/model_presets", response_model=dict)
async def load_model_presets():
    """
    Retrieve common hyperparameter presets for various models to allow easy starting points.
    """
    return {"status": "success"}
