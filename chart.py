import plotly.express as px
import pandas as pd

# ---------------- TIME SERIES ----------------
def plot_time_series(df, state):
    if state != "All States":
        df = df[df["state"] == state]

    fig = px.line(df, x="year", y="fatalities", title="")
    return fig

# ---------------- EVENT STUDY ----------------
def plot_event_study(df):
    df = df.sort_values("event_time")
    fig = px.line(df, x="event_time", y="marijuana", markers=True)
    fig.add_vline(x=0, line_dash="dash")
    return fig

# ---------------- AGE ----------------
def plot_age_distribution(df):
    grouped = df.groupby("age_group")["cases"].sum().reset_index()
    fig = px.bar(grouped, x="age_group", y="cases")
    return fig

# ---------------- GENDER ----------------
def plot_gender(df):
    grouped = df.groupby("sex")["cases"].sum().reset_index()
    fig = px.bar(grouped, x="sex", y="cases")
    return fig

# ---------------- RACE ----------------
def plot_race(df):
    grouped = df.groupby("race_clean")["cases"].sum().reset_index()
    fig = px.bar(grouped, x="race_clean", y="cases")
    return fig

# ---------------- MAP ----------------
def plot_map():
    # Simplified placeholder
    import plotly.express as px
    df = px.data.election()
    fig = px.choropleth(df, locations="district", locationmode="USA-states", color="total")
    return fig
