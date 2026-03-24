
import streamlit as st
import matplotlib.pyplot as plt
from agent.agent import AirQualityAgent

st.set_page_config(page_title="Urban Air Quality AI Agent", layout="wide")

st.title("Urban Air Quality Pattern Detection Dashboard")
st.markdown("### AI Agent Prototype (Perception → Reasoning → Action)")

agent = AirQualityAgent()

if st.button("Run AI Agent"):
    data = agent.run()

    st.success("Agent execution completed")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Pollution Pattern Clusters")
        fig, ax = plt.subplots()
        ax.scatter(data['pm25'], data['pm10'], c=data['Cluster'])
        ax.set_xlabel("PM2.5")
        ax.set_ylabel("PM10")
        ax.set_title("PM2.5 vs PM10 Clusters")
        st.pyplot(fig)

    with col2:
        st.subheader("Detected Anomalies")
        st.write(data[data['Anomaly']])

    st.subheader("Dataset Summary")
    st.write(data.describe())
