from fastapi import FastAPI
import fetch_tweets as ft
import csv
import os
import json

app = FastAPI()


def make_json(csvFilePath, jsonFilePath, tweets):
     
    # create a dictionary
    data = {}
    print("making json file")
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        cnt = 0
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            # key = rows['No']
            key = cnt
            temp = dict()
            print(tweets[cnt])
            temp["tweet"] = tweets[cnt][1]
            data[key] = rows
            data[key].update(temp)
            cnt += 1
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

# def add_tweet(jsonFilePath, tweets):
#     with open(jsonFilePath) as json_file:
#         data = json.load(json_file)
#     cnt = 0
#     for tweet in tweets:
#         temp["tweet"] = 
#         data[cnt]= tweet
#         cnt += 1

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

@app.get("/topic/{Topic}")
def topic(Topic: str, models: str):
    models = models.split(',')
    print(models)
    tweets = ft.get_tweets(Topic)
    # print(tweets)
    
    filename = "new_tweets.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(tweets)
    
    os.system("python3 ./code/preprocess.py new_tweets.csv")
    if "nb" in models:
        os.system("python3 ./code/naivebayes.py")
        make_json('./naivebayes.csv', './nb.json', tweets)
        # add_tweet('./nb.json', tweets)
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
    # tweets = ft.get_tweets(twwet)
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
