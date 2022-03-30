from fastapi import FastAPI
import fetch_tweets as ft
import csv
import os
import json

app = FastAPI()


def make_json(csvFilePath, jsonFilePath, tweets):
    
    data = {}
    print("making json file")
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        cnt = 0
        for rows in csvReader:
            key = cnt
            temp = dict()
            # print(tweets[cnt])
            temp["tweet"] = tweets[cnt][1]
            data[key] = rows
            data[key].update(temp)
            cnt += 1
 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

@app.get("/topic/{Topic}")
def topic(Topic: str, models: str):
    models = models.split(',')
    print(models)
    tweets = ft.get_tweets(Topic)
    print(tweets)
    filename = "new_tweets.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(tweets)
    
    os.system("python3 ./code/preprocess.py new_tweets.csv")
    if "bl" in models:
        os.system("python3 ./code/baseline.py")
        make_json('./baseline.csv', './bl.json', tweets)
        with open('bl.json') as json_file:
            data = json.load(json_file)
        return data
    if "svm" in models:
        os.system("python3 ./code/svm.py")
        make_json('./svm.csv', './svm.json', tweets)
        with open('svm.json') as json_file:
            data = json.load(json_file)
        return data
    if "dt" in models:
        os.system("python3 ./code/decisiontree.py")
        make_json('./decisiontree.csv', './dt.json', tweets)
        with open('dt.json') as json_file:
            data = json.load(json_file)
        return data


@app.get("/tweet/{tweet}")
def topic(tweet: str, models: str):
    models = models.split(',')
    print(models)
    # tweets = ft.get_tweets(Topic)
    tweets = [[0, tweet]]
    
    filename = "new_tweets.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(tweets)
    
    os.system("python3 ./code/preprocess.py new_tweets.csv")
    if "bl" in models:
        os.system("python3 ./code/baseline.py")
        make_json('./baseline.csv', './bl.json', tweets)
        with open('bl.json') as json_file:
            data = json.load(json_file)
        return data
    if "svm" in models:
        os.system("python3 ./code/svm.py")
        make_json('./svm.csv', './svm.json', tweets)
        with open('svm.json') as json_file:
            data = json.load(json_file)
        return data
    if "dt" in models:
        os.system("python3 ./code/decisiontree.py")
        make_json('./decisiontree.csv', './dt.json', tweets)
        with open('dt.json') as json_file:
            data = json.load(json_file)
        return data
