import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Initialize Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)
    return score['compound']

# Function to save entries and analyze them
def save_entry(entry, date, sentiment_score):
    # Check if the file exists, if not, create an empty dataframe
    if os.path.exists("mood_data.csv"):
        data = pd.read_csv("mood_data.csv")
    else:
        data = pd.DataFrame(columns=["Date", "Entry", "Sentiment"])

    # Create a new entry and append it to the dataframe
    new_data = pd.DataFrame({"Date": [date], "Entry": [entry], "Sentiment": [sentiment_score]})
    data = pd.concat([data, new_data], ignore_index=True)

    # Save the updated dataframe to a CSV file
    data.to_csv("mood_data.csv", index=False)
    return data

# Function to clean the dataset
def clean_data(data):
    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

    # Remove rows with invalid dates
    data.dropna(subset=['Date'], inplace=True)

    # Remove duplicates based on 'Entry' and 'Date'
    data.drop_duplicates(subset=['Entry', 'Date'], keep='last', inplace=True)

    # Reset index after cleaning
    data.reset_index(drop=True, inplace=True)
    return data

# Plot mood trends
def plot_mood_trends(data):
    # Convert 'Date' column to datetime if not already
    data['Date'] = pd.to_datetime(data['Date'])

    # Set 'Date' as index
    data.set_index('Date', inplace=True)

    # Plot rolling average of sentiment scores over a 7-day window
    data['Sentiment'].rolling(window=7).mean().plot(title="Mood Trends Over Time", figsize=(10,6))
    plt.xlabel("Date")
    plt.ylabel("Mood Score (Sentiment)")
    plt.show()

# Descriptive statistics for sentiment scores
def show_statistics(data):
    print("Descriptive Statistics:")
    print(data["Sentiment"].describe())

# Plot sentiment score distribution
def plot_sentiment_distribution(data):
    plt.figure(figsize=(8, 6))
    plt.hist(data['Sentiment'], bins=20, color='skyblue', edgecolor='black')
    plt.title("Distribution of Sentiment Scores")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.show()

# Simulating user input in Google Colab
entry = input("Write about your day: ")  # Simulate user input
submit = input("Press enter to submit entry.")  # Simulate submit button

if submit and entry:
    sentiment_score = analyze_sentiment(entry)
    date = datetime.now().strftime("%Y-%m-%d")
    data = save_entry(entry, date, sentiment_score)
    print(f"Your entry has been saved!\nSentiment Score: {sentiment_score}")

    # Display sentiment score and recent entries
    print("Recent Entries:")
    print(data.tail(5))  # Show the latest 5 entries

    # Clean the dataset before displaying or analyzing further
    cleaned_data = clean_data(data)

    # Display cleaned data and EDA results
    print("Cleaned Data:")
    print(cleaned_data.tail(5))  # Show the latest 5 cleaned entries

    # Display Descriptive Statistics
    show_statistics(cleaned_data)

    # Display Mood Trends
    plot_mood_trends(cleaned_data)

    # Display Sentiment Score Distribution
    plot_sentiment_distribution(cleaned_data)

else:
    print("Please write something to submit.")

print("Your privacy matters! Your journal is safe and can be deleted anytime.")
