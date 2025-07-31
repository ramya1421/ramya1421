# Smart Disaster Response System - Code Skeleton (AWS-integrated)

# --- SETUP ---
import boto3
import requests
import json
import time
import logging
import os
import pandas as pd

from botocore.exceptions import NoCredentialsError
from transformers import pipeline
from PIL import Image

# --- CONFIGURATION ---
AWS_REGION = 'us-east-1'
S3_BUCKET = 'your-disaster-project-bucket'
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:123456789012:DisasterAlerts'

# --- AWS CLIENTS ---
s3 = boto3.client('s3')
comprehend = boto3.client('comprehend', region_name=AWS_REGION)
sns = boto3.client('sns', region_name=AWS_REGION)
rekognition = boto3.client('rekognition', region_name=AWS_REGION)

# --- SOCIAL MEDIA DATA PROCESSING (Simulated) ---
def extract_disaster_tweets(sample_texts):
    relevant_tweets = []
    for text in sample_texts:
        result = comprehend.detect_sentiment(Text=text, LanguageCode='en')
        sentiment = result['Sentiment']
        if sentiment in ['NEGATIVE', 'MIXED']:
            relevant_tweets.append(text)
    return relevant_tweets

# --- SATELLITE IMAGE ANALYSIS ---
def analyze_satellite_image_local(image_path):
    with open(image_path, 'rb') as image_file:
        response = rekognition.detect_labels(
            Image={'Bytes': image_file.read()},
            MaxLabels=10,
            MinConfidence=80
        )
    labels = [label['Name'] for label in response['Labels']]
    return labels

# --- ALERT SYSTEM ---
def send_alert(message):
    try:
        response = sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject='Disaster Alert!'
        )
        print("[ALERT SENT]", response)
    except Exception as e:
        logging.error(f"Error sending alert: {e}")

# --- MAIN WORKFLOW ---
if __name__ == '__main__':
    print("[INFO] Starting Disaster Detection Pipeline...")

    # 1. Simulate social media text
    tweets = [
        "Floods have destroyed all roads in Chennai. No power or food.",
        "Beautiful day in Hyderabad!",
        "Need help in Delhi, earthquake tremors just hit us.",
    ]
    critical_tweets = extract_disaster_tweets(tweets)
    print("[INFO] Critical tweets:", critical_tweets)

    # 2. Analyze satellite image
    labels = analyze_satellite_image_local('sample_satellite_image.jpg')
    print("[INFO] Detected labels in image:", labels)

    # 3. Trigger alert if damage-related keywords are found
    if 'Flood' in labels or len(critical_tweets) > 0:
        message = f"Disaster Detected! \nLabels: {labels}\nTweets: {critical_tweets}"
        send_alert(message)
    else:
        print("[INFO] No immediate disaster detected.")
