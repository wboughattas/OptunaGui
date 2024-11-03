from pydantic import BaseModel
from typing import List, Dict


class ProgressVisualizationResponse(BaseModel):
    """
    Model for providing data for visualizing optimization progress.

    - **trials**: List of trials with scores and other relevant metrics, useful for creating convergence plots.

    Example:
    ```json
    {
      "trials": [
        { "trial_id": 1, "score": 0.82 },
        { "trial_id": 2, "score": 0.85 }
      ]
    }
    ```
    """
    trials: List[Dict[str, float]]


class ParameterSpaceVisualizationRequest(BaseModel):
    """
    Model for specifying parameters for visualizing the parameter space.

    - **parameters**: List of parameters to include in the visualization plot.

    Example:
    ```json
    {
      "parameters": ["learning_rate", "max_depth"]
    }
    ```
    """
    parameters: List[str]


class ParameterSpaceVisualizationResponse(BaseModel):
    """
    Model for returning the generated parameter space visualization.

    - **visualization_url**: URL to access the generated visualization.

    Example:
    ```json
    {
      "visualization_url": "/visualizations/parameter_space_plot.png"
    }
    ```
    """
    visualization_url: str
