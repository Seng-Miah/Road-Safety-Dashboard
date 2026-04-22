def apply_filters(df, person_type, substance):
    
    if person_type != "All" and "per_type_label" in df.columns:
        df = df[df["per_type_label"] == person_type]

    if substance == "alcohol":
        df = df[(df["alcohol"] == 1) & (df["marijuana"] == 0)]
    elif substance == "marijuana":
        df = df[(df["marijuana"] == 1) & (df["alcohol"] == 0)]
    elif substance == "both":
        df = df[(df["marijuana"] == 1) & (df["alcohol"] == 1)]
    elif substance == "none":
        df = df[(df["marijuana"] == 0) & (df["alcohol"] == 0)]

    return df
