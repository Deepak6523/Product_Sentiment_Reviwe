from vader_sentiment.vader_sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

analyzer = SentimentIntensityAnalyzer()

while True:
    print("press 1 for review : ")
    print("press any key to exit : ")
    x = input("Enter your choice: ")
    if x == '1':
        text = input("Please enter the text for review: ")
        sentiment = analyzer.polarity_scores(text)

        try:
            categories = ['Very Bad Review 😡🤬', 'Bad Review 😔😩', 'Neutral 😉🤓', 'Positive 😍😘🥰', 'Highly Positive 🤩😇🥳']
            scores = [0, 0, 0, 0, 0]  

            if sentiment['compound'] >= 0.075:
                print("Highly Positive 🤩\n")
                scores[4] += 1
            elif sentiment['compound'] >= 0.05:
                print("Positive 😍\n")
                scores[3] += 1
            elif sentiment['compound'] < 0.05 and sentiment['compound'] > -0.01:
                print("Neutral 😉🤓\n")
                scores[2] += 1
            elif sentiment['compound'] <= -0.01:
                print("Bad Review 😔😩\n")
                scores[1] += 1
            else:
                print("Very Bad Review 😡🤬\n")
                scores[0] += 1

            plt.figure(figsize=(10, 5))
            plt.bar(categories, scores, color=['red', 'orange', 'blue', 'green', 'purple'])
            plt.xlabel('Sentiment Categories')
            plt.ylabel('Number of Reviews')
            plt.title('Sentiment Analysis Review Graph')
            plt.show()

        except Exception as e:
            print(e)
    else:
        print("Exited program")
        break

