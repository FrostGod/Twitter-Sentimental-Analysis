from fastapi import FastAPI
import fetch_tweets as ft
import csv

app = FastAPI()

@app.get("/topic/{Topic}")
def about(Topic: str):
    tweets = ft.get_tweets(Topic)
    print(tweets)
    
    filename = "new_tweets.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(tweets)

    return {"Data": "Got"}

# inventory = {
#     1: {
#         "name": "item1",
#         "price": 2
#     }
# }

@app.get("/item/{item_id}")
def about(item_id: int):
    return inventory[item_id]
