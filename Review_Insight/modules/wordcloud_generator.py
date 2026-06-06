from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate(text):

    wc = WordCloud(
        width=800,
        height=400
    ).generate(text)

    fig, ax = plt.subplots()

    ax.imshow(wc)

    ax.axis("off")

    return fig