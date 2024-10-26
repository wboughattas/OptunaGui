import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics, model_selection
import streamlit as st
from utils.data_loader import load_iris_data


class IrisModel:
    def objective(self, trial):
        model_type = st.session_state["model_type"]
        split_ratio = st.session_state["split_ratio"]
        random_state = st.session_state["random_state"]
        X, y = load_iris_data()
        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=split_ratio,
                                                                            random_state=random_state)

        if model_type == "XGBoost":
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

        st.session_state["conf_matrix"] = metrics.confusion_matrix(y_test, y_pred)
        st.session_state["class_report"] = metrics.classification_report(y_test, y_pred, output_dict=True)

        return score
