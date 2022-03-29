from fastapi import FastAPI
import fetch_tweets as ft
import csv
import os

app = FastAPI()

@app.get("/topic/{Topic}")
def topic(Topic: str, models: str):
    # print(models)
    models = models.split(',')
    print(models)
    tweets = ft.get_tweets(Topic)
    print(tweets)
    
    filename = "new_tweets.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(tweets)
    
    os.system("python3 ./code/preprocess.py new_tweets.csv")
    if "nb" in models:
        os.system("python3 ./code/naivebayes.py")
    if "bl" in models:
        os.system("python3 ./code/baseline.py")
    if "svm" in models:
        os.system("python3 ./code/svm.py")
    if "dt" in models:
        os.system("python3 ./code/decisiontree.py")
    if "rf" in models:
        os.system("python3 ./code/randomforest.py")
    
    return {"Data": "Got"}

@app.get("/tweet/{tweet}")
def tweet(tweet: str, models: str):
    # print(models)
    models = models.split(',')
    print(models)
    tweets = ft.get_tweets(Topic)
    print(tweets)
    
    filename = "new_tweets.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(tweets)
    
    os.system("python3 ./code/preprocess.py new_tweets.csv")
    if "nb" in models:
        os.system("python3 ./code/naivebayes.py")
    if "bl" in models:
        os.system("python3 ./code/baseline.py")
    if "svm" in models:
        os.system("python3 ./code/svm.py")
    if "dt" in models:
        os.system("python3 ./code/decisiontree.py")
    if "rf" in models:
        os.system("python3 ./code/randomforest.py")
    
    return {"Data": "Got"}

# inventory = {
#     1: {
#         "name": "item1",
#         "price": 2
#     }
# }
