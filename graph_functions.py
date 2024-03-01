import streamlit as st
import networkx as nx


def output_nodes_and_edges(graph: nx.Graph):
    st.write(graph.nodes)
    st.write(graph.edges)

def count_nodes(graph):
    num_nodes = len(graph.nodes)
    st.info(f"No_of_nodes{num_nodes}")
