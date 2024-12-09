import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Hackathon Roadmap Gantt Chart", layout="wide")

# Data for Gantt chart
data = {
    "Task": [
        "Introductory Session",
        "Idea Submissions",
        "Team Formation",
        "Ask Me Anything (AMA) Session",
        "Idea Submission Evaluation Round",
        "Initial Shortlist Announcement",
        "Prototype Development",
        "Induction Session",
        "Prototype Submissions Evaluation Round",
        "Grand Finale"
    ],
    "Start": [
        "2024-11-25 16:00",
        "2024-11-18 16:00",
        "2024-11-18 16:01",
        "2024-12-12 16:00",
        "2025-01-01 10:00",
        "2025-01-16 00:01",
        "2025-01-16 00:01",
        "2025-01-17 16:00",
        "2025-02-03 11:00",
        "2025-03-08 09:00"
    ],
    "End": [
        "2024-11-25 17:00",
        "2024-12-22 23:59",
        "2024-12-15 23:59",
        "2024-12-12 17:00",
        "2025-01-15 23:59",
        "2025-01-16 23:59",
        "2025-02-02 23:59",
        "2025-01-17 17:00",
        "2025-02-17 23:59",
        "2025-03-08 18:00"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert dates to datetime format
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

# Title
st.title("Hackathon Roadmap")

# Plot Gantt chart using Plotly Timeline
fig = px.timeline(
    df,
    x_start="Start",
    x_end="End",
    y="Task",
    title="Hackathon Roadmap Gantt Chart",
    labels={"Task": "Activities"},
    color="Task"
)

# Update layout for better readability
fig.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Tasks",
    showlegend=False,
    xaxis=dict(type="date"),
    yaxis=dict(autorange="reversed"),
    plot_bgcolor="black",
    paper_bgcolor="black",
    template="plotly_dark"
)

# Display Gantt chart
st.plotly_chart(fig, use_container_width=True)
