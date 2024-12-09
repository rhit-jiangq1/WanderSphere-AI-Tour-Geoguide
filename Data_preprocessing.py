#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:00:00 2024

@author: Hemanth Bathini
"""

import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

file_path = 'flickr_photo_data.xlsx'  
df = pd.read_excel(file_path)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_comment(text):
    if pd.isnull(text):
        return ""
    text = re.sub(r'http\S+|www.\S+', '', text)
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = text.lower()
    return text.strip()

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return tokens

df['Cleaned_Comment'] = df['Comment'].apply(clean_comment)

df['Tokens'] = df['Cleaned_Comment'].apply(preprocess_text)

output_file = 'processed_comments.xlsx'
df.to_excel(output_file, index=False)

print(f"Processed data saved to {output_file}")
