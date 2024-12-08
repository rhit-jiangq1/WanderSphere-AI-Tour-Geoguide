#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:00:00 2024

@author: Hemanth Bathini
"""

import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline

import nltk
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):

    if not text:
        return ""
    text = text.lower()
    # Removing URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    # Removing special characters and numbers
    text = re.sub(r"[^a-z\s]", '', text)
    # Tokenizing
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

def analyze_sentiment_vader(comments):
    analyzer = SentimentIntensityAnalyzer()
    results = []
    for comment in comments:
        scores = analyzer.polarity_scores(comment)
        sentiment = "Neutral"
        if scores['compound'] >= 0.05:
            sentiment = "Positive"
        elif scores['compound'] <= -0.05:
            sentiment = "Negative"
        results.append({'comment': comment, 'sentiment': sentiment, 'score': scores['compound']})
    return results

def analyze_sentiment_textblob(comments):
    results = []
    for comment in comments:
        blob = TextBlob(comment)
        sentiment = "Neutral"
        if blob.sentiment.polarity > 0:
            sentiment = "Positive"
        elif blob.sentiment.polarity < 0:
            sentiment = "Negative"
        results.append({'comment': comment, 'sentiment': sentiment, 'score': blob.sentiment.polarity})
    return results

def analyze_sentiment_bert(comments):
    classifier = pipeline("sentiment-analysis")
    results = []
    for comment in comments:
        result = classifier(comment)[0]
        sentiment = result['label']
        sentiment = "Positive" if sentiment == "POSITIVE" else "Negative"
        results.append({'comment': comment, 'sentiment': sentiment, 'score': result['score']})
    return results


comments = [
    "not very good location to travel alone",
    "looks shady at night",
    "gloomy weather in december",
    "beautiful scenery and vibrant colors",
    "amazing place to visit with family!"
]

preprocessed_comments = [preprocess_text(comment) for comment in comments]

# Performing sentiment analysis
vader_results = analyze_sentiment_vader(preprocessed_comments)
textblob_results = analyze_sentiment_textblob(preprocessed_comments)
bert_results = analyze_sentiment_bert(preprocessed_comments)

# Combining results into a DataFrame
df_results = pd.DataFrame({
    'Original Comment': comments,
    'Preprocessed Comment': preprocessed_comments,
    'VADER Sentiment': [res['sentiment'] for res in vader_results],
    'VADER Score': [res['score'] for res in vader_results],
    'TextBlob Sentiment': [res['sentiment'] for res in textblob_results],
    'TextBlob Score': [res['score'] for res in textblob_results],
    'BERT Sentiment': [res['sentiment'] for res in bert_results],
    'BERT Score': [res['score'] for res in bert_results],
})

# Output the results to a CSV file
df_results.to_csv('sentiment_analysis_results.csv', index=False)

print("Sentiment analysis complete. Results saved to 'sentiment_analysis_results.csv'.")
