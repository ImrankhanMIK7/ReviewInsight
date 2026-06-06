import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from modules.sentiment import get_sentiment

st.set_page_config(
    page_title="🏨 Review_Sense_AI",
    page_icon="🏨",
    layout="wide"
)

st.markdown("""
<style>
.metric-card{
    background-color:#262730;
    padding:15px;
    border-radius:15px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.title("🏨 Hotel & Restaurant Review Analytics")
st.caption("AI Powered Customer Feedback Dashboard")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    # Merge reviews

    review_cols = []

    if "Review" in df.columns:
        review_cols.append(df["Review"].fillna(""))

    if "Review2" in df.columns:
        review_cols.append(df["Review2"].fillna(""))

    if len(review_cols) > 0:
        df["Final_Review"] = review_cols[0]

        if len(review_cols) == 2:
            df["Final_Review"] = (
                review_cols[0] + " " + review_cols[1]
            )

    else:
        st.error("Review column not found.")
        st.stop()

    # Rating

    if "rating" in df.columns:
        df["rating"] = (
            df["rating"]
            .astype(str)
            .str.extract(r'(\d+)')
            .astype(float)
        )

    # Sentiment

    df["Sentiment"] = df.apply(
        lambda row: get_sentiment(
            row["Final_Review"],
            row["rating"]
        ),
        axis=1
    )
    total = len(df)

    avg_rating = round(df["rating"].mean(),2)

    pos = len(df[df["Sentiment"]=="Positive"])
    neg = len(df[df["Sentiment"]=="Negative"])
    neu = len(df[df["Sentiment"]=="Neutral"])

    
    # Hotel Health Score

    positive_pct = (pos / total) * 100
    negative_pct = (neg / total) * 100

    health_score = (
        (avg_rating * 15)
        + (positive_pct * 0.5)
        - (negative_pct * 0.3)
    )

    health_score = max(
        0,
        min(
            100,
            round(health_score, 1)
        )
    )

    if health_score >= 90:
        health_status = "🏆 Outstanding"

    elif health_score >= 75:
        health_status = "🟢 Excellent"

    elif health_score >= 60:
        health_status = "🟡 Good"

    elif health_score >= 40:
        health_status = "🟠 Needs Improvement"

    else:
        health_status = "🔴 Critical"

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric(
        "📝 Total Reviews",
        total
    )

    c2.metric(
        "⭐ Average Rating",
        avg_rating
    )

    c3.metric(
        "😊 Positive",
        pos
    )

    c4.metric(
        "😡 Negative",
        neg
    )

    c5.metric(
        "🏨 Health Score",
        f"{health_score}/100"
    )

        
    st.divider()

    left,right = st.columns(2)

    with left:

        fig = px.pie(
            df,
            names="Sentiment",
            title="Sentiment Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        fig2 = px.histogram(
            df,
            x="rating",
            title="Rating Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.divider()


    st.subheader("☁ Review Word Cloud")

    text = " ".join(
        df["Final_Review"].astype(str)
    )

    wc = WordCloud(
        width=1200,
        height=500,
        background_color="white"
    ).generate(text)

    fig3,ax = plt.subplots(figsize=(12,5))

    ax.imshow(wc)

    ax.axis("off")

    st.pyplot(fig3)

    st.divider()
    st.subheader("🏨 Hotel Health Score")

    st.progress(health_score / 100)

    col1, col2 = st.columns([1,3])

    with col1:
        st.metric(
            "Score",
            f"{health_score}/100"
        )

    with col2:
        st.success(
            f"Overall Hotel Status : {health_status}"
        )

    st.subheader("🤖 AI Business Insight")

    positive_ratio = round(pos/total*100,1)

    if positive_ratio > 70:

        st.success(f"""
Customers are generally satisfied.

✔ Strong Areas:
- Staff Behaviour
- Overall Experience
- Location

⚠ Suggested Improvements:
- Focus on negative reviews.
- Improve consistency in service.
- Monitor recurring complaints.
""")

    else:

        st.error(f"""
Customer satisfaction needs improvement.

Top Priority:
- Food Quality
- Service Speed
- Room Maintenance

Review negative feedback carefully and address common issues.
""")

    st.divider()

    st.subheader("🔍 Search Reviews")

    keyword = st.text_input(
        "Search any keyword"
    )

    if keyword:

        result = df[
            df["Final_Review"]
            .str.contains(
                keyword,
                case=False,
                na=False
            )
        ]

        st.dataframe(
            result,
            use_container_width=True
        )

    else:

        st.dataframe(
            df,
            use_container_width=True
        )

    st.download_button(
        "📥 Download Processed CSV",
        df.to_csv(index=False),
        "processed_reviews.csv",
        "text/csv"
    )

else:

    st.info(
        "⬅ Upload your Google Review CSV or Excel file to begin."
    )