import plotly.express as px

def sentiment_chart(df):

    fig = px.pie(
        df,
        names="sentiment",
        title="Sentiment Distribution"
    )

    return fig


def rating_chart(df):

    fig = px.histogram(
        df,
        x="rating",
        title="Rating Distribution"
    )

    return fig