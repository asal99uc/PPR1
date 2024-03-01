import streamlit as st
import networkx as nx
from graph_functions import output_nodes_and_edges,count_nodes

def store_graph():
    with st.expander("Show individual lists"):
        st.json(st.session_state["node_list"], expanded=True)
        st.json(st.session_state["edge_list"], expanded=False)

    graph_dict = {
        "nodes": st.session_state["node_list"],
        "edges": st.session_state["edge_list"],
    }
    st.session_state["graph_dict"] = graph_dict

    with st.expander("Show Graph JSON", expanded=False):
        st.json(st.session_state["graph_dict"])


def analyze_graph():
    G = nx.Graph()
    graph_dict = st.session_state["graph_dict"]
    node_list = graph_dict["nodes"]
    edge_list = graph_dict["edges"]
    node_tuple_list = []
    edge_tuple_list = []

    for node in node_list:
        node_tuple = (node["name"], node)
        node_tuple_list.append(node_tuple)

    for edge in edge_list:
        edge_tuple = (edge["source"], edge["target"], edge)
        edge_tuple_list.append(edge_tuple)

    G.add_nodes_from(node_tuple_list)
    G.add_edges_from(edge_tuple_list)

    select_function = st.selectbox(label="Select function",
                                   options=["Output nodes and edges", "Count Nodes"])
    if select_function == "Output nodes and edges":
        output_nodes_and_edges(graph=G)
    elif select_function == "Count Nodes":
        count_nodes(graph=G)

    G.add_nodes_from(node_tuple_list)
    G.add_edges_from(edge_tuple_list)

