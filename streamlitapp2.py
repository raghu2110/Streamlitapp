import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import graphs,charts,animated,Formats

st.title('Hierarchical Graph')
st.caption('This graph shows the hierarchical relationship between employees and their managers.')

tabSource, tabGraph, tabFormat, tabChart, tabAnimated = st.tabs(['Source', 'Graph', 'Format', 'Chart', 'animated'])

with tabSource:
    df = pd.read_csv('Formats/Data/employee-manager.csv', header=0).convert_dtypes()
    st.dataframe(df)

with tabGraph:
    graph = graphs.getEdges(df)
    url = graphs.getUrl(graph)
    st.link_button('Visualize Graph', url)
    st.graphviz_chart(graph)

with tabChart:
    labels = df[df.columns[0]]
    parents = df[df.columns[1]]

    sel = st.selectbox(
        "Select a chart type:",
        options=["Treemap", "Icicle", "Sunburst", "Sankey"])
    if sel == "Treemap":
        fig = charts.makeTreemap(labels, parents)
    elif sel == "Icicle":
        fig = charts.makeIcicle(labels, parents)
    elif sel == "Sunburst":
        fig = charts.makeSunburst(labels, parents)
    else:
        fig = charts.makeSankey(labels, parents)
    st.plotly_chart(fig, use_container_width=True)

# show as D3 animated chart
with tabAnimated:
    sel = st.selectbox(
        "Select a D3 chart type:",
        options=["Collapsible Tree", "Linear Dendrogram",
            "Radial Dendrogram", "Network Graph"])
    if sel == "Collapsible Tree":
        filename = animated.makeCollapsibleTree(df)
    elif sel == "Linear Dendrogram":
        filename = animated.makeLinearDendrogram(df)
    elif sel == "Radial Dendrogram":
        filename = animated.makeRadialDendrogram(df)
    else:
        filename = animated.makeNetworkGraph(df)

with open(filename, 'r', encoding='utf-8') as f:
    components.html(f.read(), height=2200, width=1000)