import streamlit as st
from streamlit_option_menu import option_menu
from tabs import upload_graph
from export import export_tab
from person import save_node, save_edge, create_node, node_relation
from visualize import visualize
from analyze import store_graph, analyze_graph


tab_list = ["Import Graph",
            "Create Nodes",
            "Create Relations",
            "Store the Graph",
            "graph visualization",
            "analyze graph",
            "Export the Graph"]

if __name__ == '__main__':
    if "node_list" not in st.session_state:
        st.session_state["node_list"] = []
    if "edge_list" not in st.session_state:
        st.session_state["edge_list"] = []
    if "graph_dict" not in st.session_state:
        st.session_state["graph_dict"] = []

    #st.title("abc")
    #(import_graph_tab, create_node_tab, create_relation_tab, store_graph_tab, visualize_graph_tab, analyze_graph_tab, export_graph_tab) = (
      #       st.tabs(tab_list))

    with st.sidebar:
        selected = option_menu("Main Menu",
                               tab_list,  # required
                                icons=["house", "book", "envelope"],  # optional
                                menu_icon="cast",
                                default_index =1, orientation="vertical")
        st.write(selected)

    if selected == "Import Graph":
        upload_graph()

    if selected == "Create Nodes":
        create_node()

    if selected == "Create Relations":
        node_relation()

    if selected == "Store the Graph":
        store_graph()

    if selected == "graph visualization":
        visualize()

    if selected == "analyze graph":
        analyze_graph()

    if selected == "Export the Graph":
        export_tab()