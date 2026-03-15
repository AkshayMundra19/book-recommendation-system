import pandas as pd

def recommend_books(df, language, genre):

    filtered = df[
        (df["language"].str.lower() == language.lower()) &
        (df["genre"].str.lower() == genre.lower())
    ]

    if filtered.empty:
        return []

    return filtered["title"].sample(
        min(5, len(filtered))
    ).tolist()