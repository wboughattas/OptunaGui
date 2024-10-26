import streamlit as st


class SessionManager:
    def __init__(self):
        pass

    def initialize_session_state(self):
        if "studies" not in st.session_state:
            st.session_state["studies"] = []
        if "expanded_study_id" not in st.session_state:
            st.session_state["expanded_study_id"] = None
        if "selected_study_id" not in st.session_state:
            st.session_state["selected_study_id"] = None
        if "selected_study_name" not in st.session_state:
            st.session_state["selected_study_name"] = None
        if "model_type" not in st.session_state:
            st.session_state["model_type"] = "XGBoost"
        if "split_ratio" not in st.session_state:
            st.session_state["split_ratio"] = 0.2
        if "random_state" not in st.session_state:
            st.session_state["random_state"] = 42
