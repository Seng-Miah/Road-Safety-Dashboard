import pandas as pd

def load_data():
    return {
        "state": pd.read_csv("data/state_year.csv"),
        "event": pd.read_csv("data/event_study.csv"),
        "age": pd.read_csv("data/age_person_dist.csv"),
        "gender": pd.read_csv("data/gender_dist.csv"),
        "race": pd.read_csv("data/race_dist.csv"),
    }
