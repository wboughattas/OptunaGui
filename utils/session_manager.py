import streamlit as st

from models.models import Run, Runs
from utils import *


class SessionManager:
    def __init__(self):
        if "runs" not in st.session_state:
            st.session_state["runs"] = []
        if "requires_load_runs" not in st.session_state:
            st.session_state["requires_load_runs"] = True
        if "new_run_name" not in st.session_state:
            st.session_state["new_run_name"] = ""
        if "selected_run" not in st.session_state:
            st.session_state["selected_run"] = None
        if "expanded_run" not in st.session_state:
            st.session_state["expanded_run"] = None
        if "selected_trial" not in st.session_state:
            st.session_state["selected_trial"] = None
        if "run_to_delete" not in st.session_state:
            st.session_state["run_to_delete"] = None
        if "model_type" not in st.session_state:
            st.session_state["model_type"] = "XGBoost"
        if "split_ratio" not in st.session_state:
            st.session_state["split_ratio"] = 0.2
        if "random_state" not in st.session_state:
            st.session_state["random_state"] = 42
        if "conf_matrix" not in st.session_state:
            st.session_state["conf_matrix"] = None
        if "class_report" not in st.session_state:
            st.session_state["class_report"] = None

    @staticmethod
    def create_new_session_state(key: str, value):
        st.session_state[key] = value
        st.toast(f"Created new {key} state with {value}")
        return value

    @staticmethod
    def update_session_state(key: str, value):
        assert key in st.session_state, f"{key} not in session state"
        old_value = deep_get(st.session_state, key)
        deep_insert(st.session_state, key, value)
        return old_value

    @staticmethod
    def get_session_state(key: str, default=None):
        value = deep_get(st.session_state, key, default)
        return value

    @staticmethod
    def delete_session_state(key: str):
        value = deep_delete(st.session_state, key)
        return value

    @staticmethod
    def add_runs(runs: Runs):
        st.session_state["runs"] = runs
        return runs

    @staticmethod
    def add_run(run: Run):
        st.session_state["runs"].append(run)
        return run

    @staticmethod
    def delete_run(study_id: int):
        run = next((run for run in st.session_state["runs"] if run.study._study_id == study_id), None)
        st.session_state["runs"] = [run for run in st.session_state["runs"] if run.study._study_id != study_id]
        return run

    @staticmethod
    def add_trials(study_id, trials):
        index = next((i for i, run in enumerate(st.session_state["runs"]) if run["study"]._study_id == study_id), None)
        st.session_state["runs"][index]["trials"] = trials
        run = st.session_state["runs"][index]
        return run

    @staticmethod
    def delete_trials(study_id: int):
        index = next((i for i, run in enumerate(st.session_state["runs"]) if run["study"]._study_id == study_id), None)
        st.session_state["runs"][index]["trials"] = []
        run = st.session_state["runs"][index]
        return run
