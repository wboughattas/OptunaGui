from pydantic import BaseModel
from typing import List, Dict, Optional


class ExperimentConfig(BaseModel):
    """
    Model for initializing a new experiment configuration.

    - **experiment_name**: The name of the experiment.
    - **_model_type**: The type of model to use (e.g., "XGBoost", "LightGBM").
    - **dataset_id**: Identifier for the dataset to be used in the experiment.
    - **split_ratio**: Ratio for splitting the dataset into training and test sets.
    - **hyperparameters**: Hyperparameters for tuning, defined with ranges.

    Example:
    ```json
    {
      "experiment_name": "Experiment 1",
      "_model_type": "XGBoost",
      "dataset_id": "1234",
      "split_ratio": 0.2,
      "hyperparameters": {
        "learning_rate": [0.01, 0.1],
        "max_depth": [3, 10]
      }
    }
    ```
    """
    experiment_name: str
    _model_type: str
    dataset_id: str
    split_ratio: float
    hyperparameters: Dict[str, List[float]]


class FeatureSelectionConfig(BaseModel):
    """
    Model for configuring feature selection and transformations.

    - **feature_selection**: List of features to be included in the model.
    - **transformations**: Dictionary specifying transformations for each feature, e.g., normalization and encoding.

    Example:
    ```json
    {
      "feature_selection": ["feature1", "feature2", "feature3"],
      "transformations": {
        "normalize": "minmax",
        "encoding": "one-hot"
      }
    }
    ```
    """
    feature_selection: List[str]
    transformations: Dict[str, Optional[str]]


class ModelPresetsResponse(BaseModel):
    """
    Model for returning preset hyperparameters for various models.

    - **presets**: Dictionary containing default fixed hyperparameter values for each model type.

    Example:
    ```json
    {
      "presets": {
        "XGBoost": {
          "learning_rate": 0.1,
          "max_depth": 6
        },
        "LightGBM": {
          "num_leaves": 31,
          "boosting_type": "gbdt"
        }
      }
    }
    ```
    """
    presets: Dict[str, Dict[str, float]]
