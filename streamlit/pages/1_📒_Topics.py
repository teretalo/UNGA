import sys
sys.path.append("..")
from graph_formating import generate_graph, select_topic, select_continent
from topicplot import display_topics, select_topic_hist
import streamlit as st
from shapely import geos

st.set_page_config(layout="wide")

def topics_main():
    with st.form('form'):
        st.header('How did the agenda change over time for continents')
        selected_topic = select_topic()
        selected_continent = select_continent()
        st.session_state.selected_topic = selected_topic
        st.session_state.selected_continent = selected_continent
        graph_button = st.form_submit_button('Plot the graph')

    if graph_button:
        generate_graph(st.session_state.selected_topic, st.session_state.selected_continent )

    st.empty()
    st.empty()
    st.empty()
    st.empty()

    st.header('What were the main topics for each country in each decade')
    display_topics()

    st.header('How did the underlying vocabulary change over time')
    words_list = select_topic_hist()
    st.write(words_list)

topics_main()
