from vader_sentiment.vader_sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
while(True):
    print("press 1 for review : ")
    print("press any key to exit : ")
    x=input("enter your choice == ")
    if x == '1':
        text = input("Please enter the text for reviwe : ")
        sentiment = analyzer.polarity_scores(text)
        try: 
            
            if sentiment['compound'] >= 0.075:
                print("highly positive 🤩\n")
            elif sentiment['compound'] >= 0.05:
                print("positive 😍\n")
            elif sentiment['compound'] < 0.05:
                print("bad reviwe 😔😩\n")
            elif sentiment['compound'] <= -0.01:
                print("very bad reviwe 😡🤬\n")
            else:
                print("neutral")
        except Exception as e:
            print(e)
    else:
        print("exited program")
        break