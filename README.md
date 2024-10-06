Sentiment Analysis with Emoji-Based Visualization

This Python project provides a simple and interactive way to analyze the sentiment of user-input text using the vaderSentiment library. The application classifies the text into different sentiment categories and displays a real-time graph with emoji labels for better visual representation.

Project Overview
The application uses the SentimentIntensityAnalyzer from the vaderSentiment library to classify the user-provided text into one of the following categories:

Very Bad Review 😡🤬
Bad Review 😔😩
Neutral 😉🤓
Positive 😍
Highly Positive 🤩
The program also dynamically updates a bar chart that visually shows the number of reviews for each sentiment category, making it easy to see the distribution of sentiments over time.

Features
Interactive Text Input: The program prompts users to enter a review and classifies it in real-time.
Emoji-Based Sentiment Labels: The sentiment is represented using emojis for a more intuitive and engaging display.
Dynamic Graph Visualization: After each sentiment analysis, a bar chart is displayed showing the distribution of sentiments.
Easy-to-Use Interface: The program runs in a loop, allowing users to analyze multiple texts until they choose to exit.
Code Explanation
Initialization:
The program imports the necessary libraries: vaderSentiment for sentiment analysis and matplotlib.pyplot for visualization.
A SentimentIntensityAnalyzer object is created to evaluate the sentiment of the text input.
User Input Handling:
The program runs in a while loop, prompting the user to enter a choice:
Press 1 to input a text for review.
Press any other key to exit the program.
Sentiment Analysis:
If the user chooses to input a text, the program calculates the sentiment scores using analyzer.polarity_scores(text).
The sentiment is categorized based on the compound score:
compound >= 0.075 ➔ Highly Positive 🤩
compound >= 0.05 ➔ Positive 😍
compound < 0.05 and compound > -0.01 ➔ Neutral 😉🤓
compound <= -0.01 ➔ Bad Review 😔😩
Else ➔ Very Bad Review 😡🤬
Graph Visualization:
After categorizing the sentiment, a bar chart is generated using matplotlib.
Each sentiment category has a specific color and the emoji labels are used as x-axis labels.
The graph displays the number of reviews for each sentiment category based on user inputs.
Program Exit:
If the user chooses to exit, the program gracefully ends with a message indicating the exit.
