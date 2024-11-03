from fastapi import APIRouter

router = APIRouter()


@router.get("/{run_id}/model", response_model=dict)
async def export_best_model():
    """
    Export the best model configuration and parameters from a run for deployment or further experimentation.
    """
    pass


@router.get("/{experiment_id}/snapshot", response_model=dict)
async def create_snapshot():
    """
    Create a snapshot of a run’s results and settings, allowing users to compare changes or re-run configurations.
    """
    pass
