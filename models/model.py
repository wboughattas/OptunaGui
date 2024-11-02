import pandas as pd
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics, model_selection
from utils.data_loader import load_iris_data


class Model:
    def __init__(self, model_type, split_ratio, random_state):
        self.model_type = model_type
        self.split_ratio = split_ratio
        self.random_state = random_state
        self.results = []

    def objective(self, trial):
        X, Y = load_iris_data()
        X_train, X_test, y_train, y_test = model_selection.train_test_split(
            X, Y,
            test_size=self.split_ratio,
            random_state=self.random_state
        )

        if self.model_type == "XGBoost":
            params = {
                "n_estimators": trial.suggest_int("n_estimators", 50, 200),
                "max_depth": trial.suggest_int("max_depth", 3, 10),
                "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3)
            }
            model = xgb.XGBClassifier(**params, use_label_encoder=False, eval_metric="mlogloss")
        else:
            params = {
                "n_estimators": trial.suggest_int("n_estimators", 50, 200),
                "max_depth": trial.suggest_int("max_depth", 3, 10)
            }
            model = RandomForestClassifier(**params)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score = metrics.accuracy_score(y_test, y_pred)

        result = {
            "score": score,
            "conf_matrix": metrics.confusion_matrix(y_test, y_pred),
            "class_report": metrics.classification_report(y_test, y_pred, output_dict=True)
        }
        self.results.append(result)

        return score

    def get_confusion_matrix(self):
        return self.results[-1]["conf_matrix"]

    def get_classification_report(self) -> pd.DataFrame:
        return pd.DataFrame(self.results[-1]["class_report"]).transpose()
