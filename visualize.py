import streamlit as st
import graphviz

def visualize():
    with st.expander("Graphviz Visualisation"):
        graph = graphviz.Digraph()
        graph_dict = st.session_state["graph_dict"]
        node_list = graph_dict["nodes"]
        edge_list = graph_dict["edges"]
        for node in node_list:
            node_name = node["name"]
            graph.node(node_name)
        for edge in edge_list:
            source = edge["source"]
            target = edge["target"]
            label = edge["type"]
            graph.edge(source, target, label)
        st.graphviz_chart(graph)