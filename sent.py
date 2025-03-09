
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
import random
from bs4 import BeautifulSoup
import sys
import requests
def preprocess_pipeline(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()

    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    processed_text = ' '.join(lemmatized_tokens)
    return processed_text
    
text = preprocess_pipeline("I love spaghetti and meatballs")
analyzer = SentimentIntensityAnalyzer()



def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    print(scores)
    return scores['pos'], scores['neg'], scores['neu']