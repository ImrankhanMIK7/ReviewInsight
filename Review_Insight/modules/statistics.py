def summary(df):

    total = len(df)

    avg_rating = round(
        df["rating"].mean(),
        2
    )

    positive = len(
        df[df["sentiment"] == "Positive"]
    )

    negative = len(
        df[df["sentiment"] == "Negative"]
    )

    neutral = len(
        df[df["sentiment"] == "Neutral"]
    )

    return (
        total,
        avg_rating,
        positive,
        negative,
        neutral
    )