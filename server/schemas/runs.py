from pydantic import BaseModel
from typing import Dict, Optional


class RunCreateRequest(BaseModel):
    """
    Model for creating or cloning a run.

    - **experiment_id**: ID of the experiment associated with the run.
    - **clone_run_id**: Optional ID of an existing run to clone.

    Example:
    ```json
    {
      "experiment_id": "5678",
      "clone_run_id": "1234"
    }
    ```
    """
    experiment_id: str
    clone_run_id: Optional[str]


class RunCreateResponse(BaseModel):
    """
    Model for confirming the creation of a new run.

    - **run_id**: Unique identifier for the new run.
    - **status**: Status of the new run, e.g., "initialized".

    Example:
    ```json
    {
      "run_id": "7890",
      "status": "initialized"
    }
    ```
    """
    run_id: str
    status: str


class TrialInsightsResponse(BaseModel):
    """
    Model for real-time trial insights during a run.

    - **trial_id**: Unique identifier for the trial.
    - **hyperparameters**: Dictionary of hyperparameters used in the trial (fixed values).
    - **metrics**: Dictionary of metrics obtained in the trial, e.g., accuracy, loss, etc.

    Example:
    ```json
    {
      "trial_id": "4567",
      "hyperparameters": {
        "learning_rate": 0.05,
        "max_depth": 7
      },
      "metrics": {
        "accuracy": 0.85,
        "f1_score": 0.78
      }
    }
    ```
    """
    trial_id: str
    hyperparameters: Dict[str, float]
    metrics: Dict[str, float]


class RunControlRequest(BaseModel):
    """
    Model for controlling the state of a run.

    - **action**: Action to perform on the run, such as "pause", "stop", or "adjust".

    Example:
    ```json
    {
      "action": "pause"
    }
    ```
    """
    action: str


class RunControlResponse(BaseModel):
    """
    Model for confirming the action taken on a run.

    - **status**: Status message indicating the new state of the run, e.g., "paused".

    Example:
    ```json
    {
      "status": "paused"
    }
    ```
    """
    status: str
