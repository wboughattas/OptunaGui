import optuna
import pandas as pd
import streamlit as st
from config import DB_URL
from models.iris_model import IrisModel


class OptunaService:
    def __init__(self):
        self.db_url = DB_URL
        self.iris_model = IrisModel()

    def load_studies(self):
        try:
            studies = optuna.study.get_all_study_summaries(storage=self.db_url)
            # noinspection PyProtectedMember
            st.session_state["studies"] = [(study._study_id, study.study_name) for study in studies]
        except Exception as e:
            st.sidebar.error(f"Error loading studies: {e}")

    def create_new_study(self):
        new_study_name = st.session_state.get("new_study_name", "").strip()
        if new_study_name:
            try:
                # noinspection PyArgumentList
                study = optuna.create_study(storage=self.db_url, study_name=new_study_name)
                # noinspection PyProtectedMember
                st.session_state["studies"].append((study._study_id, new_study_name))
                # noinspection PyProtectedMember
                st.session_state["selected_study_id"] = study._study_id
                st.session_state["selected_study_name"] = new_study_name
                st.session_state["new_study_name"] = ""
                st.toast(f"Selected Study: {new_study_name}")
            except optuna.exceptions.DuplicatedStudyError:
                st.sidebar.error(f"A study with the name '{new_study_name}' already exists.")

    def delete_study(self, study_id, study_name):
        try:
            # noinspection PyArgumentList
            optuna.delete_study(study_name=study_name, storage=self.db_url)
            st.session_state["studies"] = [(_id, name) for _id, name in st.session_state["studies"] if _id != study_id]
            if st.session_state.get("selected_study_id") == study_id:
                st.session_state.pop("selected_study_id", None)
                st.session_state.pop("selected_study_name", None)
        except Exception as e:
            st.sidebar.error(f"Failed to delete study '{study_name}': {e}")

    def run_optimization(self):
        if not st.session_state.get("selected_study_id"):
            st.warning("Please select a study before running optimization.")
            return

        study_name = st.session_state["selected_study_name"]
        # noinspection PyArgumentList
        study = optuna.create_study(
            direction="maximize",
            storage=self.db_url,
            study_name=study_name,
            load_if_exists=True
        )

        study.optimize(self.iris_model.objective, n_trials=10)

        st.write(f"Optimization completed for Study: {study_name}")
        st.write("Best Trial Parameters:", study.best_trial.params)
        st.write("Best Accuracy Score:", study.best_value)

        if "conf_matrix" in st.session_state:
            st.subheader("Confusion Matrix")
            st.write(st.session_state["conf_matrix"])

        if "class_report" in st.session_state:
            st.subheader("Classification Report")
            st.write(pd.DataFrame(st.session_state["class_report"]).transpose())
