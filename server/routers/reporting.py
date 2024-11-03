from fastapi import APIRouter

router = APIRouter()


@router.get("/{run_id}/report", response_model=dict)
async def generate_report():
    """
    Generate an automated report summarizing the run’s best hyperparameters, performance metrics, and feature importance.
    """
    pass


@router.post("/{experiment_id}/notes", response_model=dict)
async def add_experiment_notes():
    """
    Add custom notes to an experiment for documentation and logging purposes.
    """
    pass
