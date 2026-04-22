import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.charts import (
    plot_time_series,
    plot_event_study,
    plot_age_distribution,
    plot_gender,
    plot_race,
    plot_map
)
from utils.filters import apply_filters

st.set_page_config(layout="wide")

# -------------------------------
# LOAD DATA
# -------------------------------
data = load_data()

state_df = data["state"]
event_df = data["event"]
age_df = data["age"]
gender_df = data["gender"]
race_df = data["race"]

# -------------------------------
# TITLE
# -------------------------------
st.title("Marijuana Legalization & Road Safety")
st.markdown(
"""
This dashboard explores how marijuana legalization relates to traffic fatalities
across U.S. states, including trends, geography, and demographics.
"""
)

# -------------------------------
# KPI
# -------------------------------
total_fatalities = state_df["fatalities"].sum()
st.metric("Total Fatalities (2000–2024)", f"{total_fatalities:,}")

# -------------------------------
# FILTERS
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    selected_state = st.selectbox(
        "Select State",
        ["All States"] + sorted(state_df["state"].unique())
    )

with col2:
    person_type = st.selectbox(
        "Person Type",
        ["All", "Driver", "Passenger", "Pedestrian"]
    )

with col3:
    substance = st.selectbox(
        "Substance",
        ["all", "alcohol", "marijuana", "both", "none"]
    )

# -------------------------------
# MAP + TIME SERIES
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Fatalities Over Time")
    st.plotly_chart(plot_time_series(state_df, selected_state))

with col2:
    st.subheader("Policy Map")
    st.plotly_chart(plot_map())

# -------------------------------
# EVENT STUDY
# -------------------------------
st.subheader("Event Study: Marijuana Legalization Effect")
st.plotly_chart(plot_event_study(event_df))

# -------------------------------
# APPLY FILTERS
# -------------------------------
age_df_f = apply_filters(age_df, person_type, substance)
gender_df_f = apply_filters(gender_df, person_type, substance)
race_df_f = apply_filters(race_df, person_type, substance)

# -------------------------------
# DEMOGRAPHICS
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Age Distribution")
    st.plotly_chart(plot_age_distribution(age_df_f))

with col2:
    st.subheader("Gender")
    st.plotly_chart(plot_gender(gender_df_f))

with col3:
    st.subheader("Race")
    st.plotly_chart(plot_race(race_df_f))
