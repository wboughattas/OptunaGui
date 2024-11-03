from fastapi import APIRouter

router = APIRouter()


@router.get("/{run_id}/progress", response_model=dict)
async def view_progress():
    """
    Retrieve data for plotting the optimization progress and convergence of a specific run.
    """
    pass
