from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import pandas as pd

try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()


def get_sentiment(text, rating):

    text = str(text)

    # Handle missing values
    if pd.isna(rating):
        rating = 3

    try:
        rating = float(rating)
    except:
        rating = 3

    if rating <= 2:
        return "Negative"

    elif rating >= 4:
        return "Positive"

    score = sia.polarity_scores(text)["compound"]

    if score >= 0.2:
        return "Positive"

    elif score <= -0.2:
        return "Negative"

    return "Neutral"