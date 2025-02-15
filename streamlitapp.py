import streamlit as st
st.title('Hierarchical Graph')

import pandas as pd
df = pd.read_csv('Formats/Data/employee-manager.csv', header=0).convert_dtypes()
st.dataframe(df)


import graphs
graph = graphs.getEdges(df)
st.graphviz_chart(graph)