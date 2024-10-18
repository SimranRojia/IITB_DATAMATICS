from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity

    if score > 0:
        return "positive", score
    elif score < 0:
        return "negative", score
    else:
        return "neutral", score
