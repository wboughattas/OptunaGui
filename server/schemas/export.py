from pydantic import BaseModel
from typing import Optional


class ModelExportResponse(BaseModel):
    """
    Model for the response containing a download link to the exported model.

    - **model_url**: URL for downloading the exported model.

    Example:
    ```json
    {
      "model_url": "/models/best_model_7890.pkl"
    }
    ```
    """
    model_url: str


class SnapshotCreateRequest(BaseModel):
    """
    Model for creating a snapshot of an experiment run.

    - **run_id**: ID of the run to snapshot.
    - **description**: Optional description for the snapshot.

    Example:
    ```json
    {
      "run_id": "7890",
      "description": "Snapshot before adjusting hyperparameters"
    }
    ```
    """
    run_id: str
    description: Optional[str]


class SnapshotCreateResponse(BaseModel):
    """
    Model for the response containing the snapshot details.

    - **snapshot_id**: Unique identifier for the snapshot.
    - **snapshot_url**: URL to access the snapshot.

    Example:
    ```json
    {
      "snapshot_id": "snapshot_123",
      "snapshot_url": "/snapshots/snapshot_123.json"
    }
    ```
    """
    snapshot_id: str
    snapshot_url: str
