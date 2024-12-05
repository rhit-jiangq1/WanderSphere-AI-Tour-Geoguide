#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:27:49 2024

@author: komalwavhal
"""
 
"""
1. Collect User Comments: textual data from social media

2. Preprocess the Data:
    Clean the text: Remove unwanted characters (punctuation, numbers, special symbols, etc.).
    Tokenize the text: Break down the comments into individual words or phrases.
    Lowercase: Convert all text to lowercase to avoid treating the same word in different cases as different words.
    Remove stop words: Filter out common words (e.g., "and," "is," "the") that don't contribute much to sentiment analysis.    
    
3. Sentiment Analysis:
    You can use various sentiment analysis models to determine if each comment is positive, negative, or neutral. Some popular tools/libraries include:
    
    TextBlob: A Python library that can determine the polarity of a text (ranges from -1 to 1, where negative values represent negative sentiment and positive values represent positive sentiment).
    VADER (Valence Aware Dictionary and sEntiment Reasoner): This is good for social media text and short comments, providing a compound score that can be used to classify sentiment as positive, negative, or neutral.
    Transformers (BERT-based models): For more advanced sentiment analysis, using pre-trained transformers (like BERT) can provide highly accurate results.

4. Classify Sentiment:
    Using a sentiment analysis tool, classify each comment as:
    
    Positive: If the sentiment score is above a threshold (e.g., greater than 0).
    Negative: If the sentiment score is below a threshold (e.g., less than 0).
    Neutral: If the sentiment score is close to 0 (can be used to filter out neutral comments).
    
5. Calculate Percentages:
    After classification, calculate the percentage of positive and negative comments:
    
    Positive Comments Percentage:  
    Positive Percentage  = ( Number of Positive Comments / Total Number of Comments ) × 100   
    
    
    Negative Comments Percentage: 
    Negative Percentage =  ( Number of Negative Comments / Total Number of Comments ) × 100 
    
    
    Neutral Comments Percentage (optional, if you're interested in neutral comments): 
    Neutral Percentage  = ( Number of Neutral Comments / Total Number of Comments  )  × 100  

"""


##############    Sentiment Analysis using VADER (Valence Aware Dictionary and sEntiment Reasoner):  ##############
def SA_VADER(comments):
    """
    VADER is a lexicon-based sentiment analysis tool, which is particularly useful for short texts like social media posts, tweets, and user comments.
    pip install vaderSentiment
    
    
    VADER's compound score is a single score that summarizes the overall sentiment of a text. It's a normalized score between -1 (most negative) and +1 (most positive).
   
    Thresholds:
    Positive if compound >= 0.05
    Negative if compound <= -0.05
    Neutral if -0.05 < compound < 0.05
    
    
    3. Key Differences:
    
    - VADER is based on a lexicon and rules, which is simple and fast. It is particularly suited for analyzing social media posts and short texts with emoticons or slang.
    
    - Transformers (BERT), on the other hand, uses deep learning and large pre-trained models for much more accurate and context-aware sentiment classification, especially for longer and more nuanced text.

    """
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

    
    # Initialize VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Initialize counters for sentiment
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    # Analyze sentiment for each comment
    for comment in comments:
        # Get sentiment scores for each comment
        sentiment_scores = analyzer.polarity_scores(comment)
        compound_score = sentiment_scores['compound']  # Get the compound score
    
        # Classify the sentiment based on compound score
        if compound_score >= 0.05:
            positive_count += 1
        elif compound_score <= -0.05:
            negative_count += 1
        else:
            neutral_count += 1
    
    # Calculate percentages
    total_comments = len(comments)
    positive_percentage = (positive_count / total_comments) * 100
    negative_percentage = (negative_count / total_comments) * 100
    neutral_percentage = (neutral_count / total_comments) * 100
    
    # Output the results
    print(f"Positive comments: {positive_percentage:.2f}%")
    print(f"Negative comments: {negative_percentage:.2f}%")
    print(f"Neutral comments: {neutral_percentage:.2f}%")

    

##############  Sentiment Analysis using Transformers (BERT-based models):     ##############
def SA_BERT(comments):
    """
    For more accurate and context-aware sentiment analysis, you can use a pre-trained BERT-based model like distilbert-base-uncased or bert-base-uncased from the Transformers library by Hugging Face.
    
    pip install transformers torch 
    
    Hugging Face Transformers: We're using the sentiment-analysis pipeline, which uses a pre-trained model like distilbert-base-uncased or bert-base-uncased. This model is fine-tuned for sentiment analysis tasks.
    The pipeline returns labels like POSITIVE and NEGATIVE, and also provides a confidence score (score) for the sentiment.
    
    3. Key Differences:
    
    - VADER is based on a lexicon and rules, which is simple and fast. It is particularly suited for analyzing social media posts and short texts with emoticons or slang.
    
    - Transformers (BERT), on the other hand, uses deep learning and large pre-trained models for much more accurate and context-aware sentiment classification, especially for longer and more nuanced text.

    """
    from transformers import pipeline

    # Load pre-trained sentiment analysis pipeline from Hugging Face
    classifier = pipeline("sentiment-analysis")
    

    # Initialize counters for sentiment
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    # Analyze sentiment for each comment
    for comment in comments:
        result = classifier(comment)[0]
        label = result['label']  # 'LABEL_0' -> negative, 'LABEL_1' -> positive
        score = result['score']  # Confidence score of sentiment
        print(score)
    
        # Classify the sentiment
        if label == 'POSITIVE':
            positive_count += 1
        elif label == 'NEGATIVE':
            negative_count += 1
        else:
            neutral_count += 1
    
    # Calculate percentages
    total_comments = len(comments)
    positive_percentage = (positive_count / total_comments) * 100
    negative_percentage = (negative_count / total_comments) * 100
    neutral_percentage = (neutral_count / total_comments) * 100
    
    # Output the results
    print(f"Positive comments: {positive_percentage:.2f}%")
    print(f"Negative comments: {negative_percentage:.2f}%")
    print(f"Neutral comments: {neutral_percentage:.2f}%")


##############    Sentiment Analysis using  TextBlob   ##############
def SA_TextBlob(comments):
    
    from textblob import TextBlob
    
   
    
    # Initialize counters for sentiment
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    # Analyze sentiment for each comment
    for comment in comments:
        blob = TextBlob(comment)
        sentiment_score = blob.sentiment.polarity
    
        # Classify the sentiment
        if sentiment_score > 0:
            positive_count += 1
        elif sentiment_score < 0:
            negative_count += 1
        else:
            neutral_count += 1
    
    # Calculate percentages
    total_comments = len(comments)
    positive_percentage = (positive_count / total_comments) * 100
    negative_percentage = (negative_count / total_comments) * 100
    neutral_percentage = (neutral_count / total_comments) * 100
    
    print(f"Positive comments: {positive_percentage:.2f}%")
    print(f"Negative comments: {negative_percentage:.2f}%")
    print(f"Neutral comments: {neutral_percentage:.2f}%")



 
comments =  [
    'We did the Rockefeller Center architecture tour. The key to this tour is to have a great guide, and Jonathan was that guide. It was a wonderful, informative, and educational tour. Jonathan really knew his stuff!',
    'We had the pleasure of a VIP experience led by Karmilla! The NYC skyline at night was absolutely beautiful, and the panoramic views from the Sky Lift were truly unbeatable.',
    'We visited The Top of The Rock about an hour before sunset and then took in the views whilst the sun went down. It was pretty busy and difficult to get some space but everyone was polite in taking turns for the best photos.'
]

# ['not very good locaition to travel alone',
#              'looks shady in night',
#              'gloomy weather in december']
#  

print(' ')
print(' SA_BERT model ')
SA_BERT(comments)

print(' ')
print(' SA_VADER model ')
SA_VADER(comments)

print(' ')
print(' SA_TextBlob model ')
SA_TextBlob(comments)





