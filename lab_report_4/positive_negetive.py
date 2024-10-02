negative_words=["bad","not","no","dangerous","terrible"]
positive_words=["good","happy","amazing","congratulations","thanks"]

def sentiment_analysis(negative,positive,comment):
    for item in negative:
        if item in comment:
            return "negative"
    
    for item in positive:
        if item in comment:
            return 'positive'
    return "neutral"
    
    
    
    
comm=input("enter you comment: ").lower()
sent=sentiment_analysis(negative_words,positive_words,comm)
print(comm)
if sent=='negative':
    print("this comment is negative")
elif sent=='positive':
    print("this comment is positive")
else:
    print("this comment is neutral")