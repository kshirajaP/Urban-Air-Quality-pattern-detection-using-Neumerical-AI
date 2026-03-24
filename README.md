
Urban Air Quality Pattern Detection – AI Agent Dashboard

How to run:
1. Open folder in VS Code
2. Install dependencies:
   pip install streamlit pandas numpy matplotlib scikit-learn scipy
3. Run dashboard:
   streamlit run dashboard.py

This dashboard demonstrates a working AI agent with perception, reasoning, and action.

#  Urban Air Quality Pattern Detection using Numerical AI

##  Project Overview

This project presents an **AI agent-based system** for analyzing urban air quality data using **Numerical Artificial Intelligence techniques**. The system detects **pollution patterns** and **anomalous events** from real-world air quality data and visualizes the results through an interactive dashboard.

The implementation follows an **agent architecture** consisting of:

* **Perception** → Data ingestion and preprocessing
* **Reasoning** → Pattern detection using clustering and anomaly detection
* **Action** → Visualization and presentation of insights

---

##  Objectives

* Analyze urban air quality using numerical data
* Detect hidden pollution patterns using unsupervised learning
* Identify abnormal pollution events (anomalies)
* Build an interpretable AI-agent–based analytical system
* Present results through a user-friendly dashboard

---

##  AI Techniques Used

* **K-Means Clustering** → Pattern detection in air quality data
* **Z-Score Analysis** → Anomaly detection
* **Data Preprocessing & Normalization** → Ensuring numerical consistency

---

##  Dataset

* Source: Public air quality dataset (UCI Air Quality Dataset)
* Format: Excel (.xlsx)
* Features used:

  * PM2.5 (proxy)
  * PM10 (proxy)
  * NO₂
  * SO₂ (proxy)
  * O₃ (proxy)
  * Date & Time

 Note: Some pollutant columns are mapped as proxies due to dataset constraints.

---

##  System Architecture

### 🔹 AI Agent Workflow

1. **Perception Module**

   * Loads dataset
   * Cleans and preprocesses data
   * Handles missing and invalid values

2. **Reasoning Module**

   * Converts data into numerical format
   * Applies K-Means clustering
   * Detects anomalies using Z-score

3. **Action Module (Dashboard)**

   * Displays pollution clusters
   * Shows anomaly detection results
   * Provides dataset statistics

---

##  Project Structure

```
UAQ_Agent_Dashboard/
│
├── data/
│   └── AirQualityUCI.xlsx
│
├── agent/
│   ├── perception.py
│   ├── reasoning.py
│   └── agent.py
│
├── dashboard.py
└── README.md
```

---

##  How to Run the Project

### 1️ Install Dependencies

```bash
pip install streamlit pandas numpy matplotlib scikit-learn scipy openpyxl
```

### 2 Run the Dashboard

```bash
python -m streamlit run dashboard.py
```

---

##  Features of the System

* AI-agent–based architecture
* Real dataset integration (no synthetic data)
* Pollution pattern detection using clustering
* Anomaly detection for abnormal events
* Interactive visualization using Streamlit

---

##  Limitations

* Uses proxy pollutant mappings (dataset limitation)
* No real-time data integration
* Limited temporal analysis (future scope)
* Basic anomaly detection (Z-score based)

---

##  Future Scope

* Integration with real-time APIs (e.g., OpenAQ)
* Temporal pattern analysis (daily/weekly trends)
* Advanced anomaly detection methods
* Multi-city comparative analysis
* Deployment as a web-based monitoring system

---

##  Key Learning Outcomes

* Designing AI agent architectures
* Working with real-world noisy datasets
* Applying numerical AI techniques
* Building interactive ML dashboards
* Handling data preprocessing challenges

---

##  Conclusion

This project demonstrates how **Numerical AI techniques combined with an AI agent architecture** can effectively analyze urban air quality data. The system provides meaningful insights into pollution patterns and anomalies, forming a strong foundation for future intelligent environmental monitoring systems.

---
# ⚠️ Common Errors (Quick Fix)

| Error | Fix |
|------|-----|
| git not recognized | Install Git |
| authentication failed | Use GitHub token |
| push rejected | `git pull origin main --rebase` |
---