from fastapi import APIRouter

router = APIRouter()


@router.post("/", response_model=dict)
async def create_or_clone_run():
    """
    Create a new run or clone an existing run, allowing users to duplicate configurations and tweak parameters.
    """
    pass


@router.get("/{run_id}/trials", response_model=dict)
async def view_real_time_trial_insights():
    """
    Fetch real-time trial insights and hyperparameters to display metrics being tested in real time.
    """
    pass


@router.post("/{run_id}/control", response_model=dict)
async def control_run():
    """
    Pause, stop, or adjust parameter ranges for an ongoing run to allow dynamic run management.
    """
    pass
