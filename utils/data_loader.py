import pandas as pd

def load_data():
    return {
        "state": pd.read_csv("state_year.csv"),
        "event": pd.read_csv("event_study.csv"),
        "age": pd.read_csv("age_person_dist.csv"),
        "gender": pd.read_csv("gender_dist.csv"),
        "race": pd.read_csv("race_dist.csv"),
    }
