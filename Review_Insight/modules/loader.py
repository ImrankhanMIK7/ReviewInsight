import pandas as pd

def load_data(path):
    df = pd.read_excel(path)

    df["Review"] = df["Review"].fillna("")
    df["Review2"] = df["Review2"].fillna("")

    df["final_review"] = (
        df["Review"] + " " + df["Review2"]
    )

    df["rating"] = (
        df["rating"]
        .astype(str)
        .str.extract(r'(\d+)')
        .astype(float)
    )

    return df