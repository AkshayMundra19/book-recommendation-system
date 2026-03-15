import pandas as pd

def load_dataset(path="dataset/books.csv"):
    df = pd.read_csv(path)
    df.fillna("", inplace=True)

    df["content"] = (
        df["title"] + " " +
        df["author"] + " " +
        df["genre"] + " " +
        df["description"]
    )

    return df