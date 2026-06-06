def generate_insight(df):

    positive = (
        df["sentiment"] == "Positive"
    ).sum()

    negative = (
        df["sentiment"] == "Negative"
    ).sum()

    if positive > negative:

        return """
Customers appreciate your hotel overall.
Main strengths are staff behaviour and location.

Focus on improving negative reviews
related to food quality and service speed.
"""

    return """
Customer satisfaction is below expectation.

Improve room maintenance,
service quality and food consistency.
"""