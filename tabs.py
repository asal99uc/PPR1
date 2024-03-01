import streamlit as st
import json
def upload_graph():
    uploaded_graph = st.file_uploader("Upload an existing graph", type="json")
    if uploaded_graph is not None:
        uploaded_graph_dict = json.load(uploaded_graph)
        uploaded_nodes = uploaded_graph_dict["nodes"]
        uploaded_edges = uploaded_graph_dict["edges"]
        st.write(uploaded_graph_dict)

    else:
        st.info("Please upload a graph if available")

    update_graph_button = st.button(
        "update graph via the upload",
        use_container_width=True,
        type="primary"
        )

    if update_graph_button and uploaded_graph is not None:
        st.session_state["node_list"] = uploaded_nodes
        st.session_state["edge_list"] = uploaded_edges
        graph_dict = {
            "nodes": st.session_state["node_list"],
            "edges": st.session_state["edge_list"],
        }
        st.session_state["graph_dict"] = graph_dict

        with st.expander("Show Graph JSON", expanded=False):
            st.json(st.session_state["graph_dict"])