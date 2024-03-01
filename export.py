import streamlit as st
import json

def export_tab():
    graph_string = json.dumps(st.session_state["graph_dict"])

    st.download_button(
        "Export Graph to JSON",
        file_name="graph.json",
        mime="application/json",
        data=graph_string,
        use_container_width=True,
        type="primary"
    )