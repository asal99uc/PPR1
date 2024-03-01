import streamlit as st
from model import metamodel_dict
import uuid

def print_hi(name, age):
    # Use a breakpoint in the code line below to debug your script.
    st.info(f'Hi, My name is {name} and I am {age} years old')  # Press Strg+F8 to toggle the breakpoint.
def save_node(name, age):
    node_dict = {
        "name": name,
        "age": age,
        "id": str(uuid.uuid4()),
        "type": "node"
    }
    st.session_state["node_list"].append(node_dict)
def save_edge(node1, relation, node2):
    edge_dict = {
        "source": node1,
        "target": node2,
        "type": relation,
        "id": str(uuid.uuid4()),
    }
    st.session_state["edge_list"].append(edge_dict)
def create_node():
        name_node = st.text_input("Type in the name of the node")
        age_node = int(st.number_input("Input the age of the node", value=0))
        print_hi(name_node, age_node)
        save_node_button = st.button("Store node", use_container_width=True, type="primary")
        if save_node_button:
            save_node(name_node, age_node)
        st.write(st.session_state["node_list"])

def node_relation():
    node_list = st.session_state["node_list"]
    node_name_list = []
    for node in node_list:
            node_name_list.append(node["name"])

    node1_col, relation_col, node2_col = st.columns(3)
    with node1_col:
            node1_select = st.selectbox(
                    "Select the first node",
                    options=node_name_list,
                    key="node1_select"
            )
    with relation_col:

            relation_list = metamodel_dict["edges"]

            relation_name = st.selectbox(
                    "Specify the relation",
                    options=relation_list)
    with node2_col:
            node2_select = st.selectbox(
                    "Select the second node",
                    options=node_name_list,
                    key="node2_select"
            )
    store_edge_button = st.button("Store Relation",
                                  use_container_width=True,
                                  type="primary")

    if store_edge_button:
            save_edge(node1_select, relation_name, node2_select)

    st.write(f"{node1_select} is {relation_name} {node2_select}")  # Most pythonic version
    st.write(st.session_state["edge_list"])