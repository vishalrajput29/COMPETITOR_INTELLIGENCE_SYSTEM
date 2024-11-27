# analyze_app_reviews.py
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

def fetch_app_reviews(app_url):
    response = requests.get(app_url)
    soup = BeautifulSoup(response.text, "html.parser")
    reviews = soup.find_all("div", class_="review-text")
    return [review.text for review in reviews]

def analyze_sentiment(reviews):
    return [{"review": review, "sentiment": TextBlob(review).sentiment.polarity} for review in reviews]

if __name__ == "__main__":
    APP_URL = "https://www.example.com/app-reviews"
    reviews = fetch_app_reviews(APP_URL)
    sentiment_analysis = analyze_sentiment(reviews)
    print(sentiment_analysis)
