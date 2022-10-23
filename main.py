from flask import Flask,jsonify,request

import pandas as pd
import csv

df = pd.read_csv("articles.csv")
app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "df" : df,
        "message" : "success"
    }),201


liked_articles = []
disliked_articles = []

@app.route("/get-article")
def get_movies():
    return jsonify({
        "data" : df[0],
        "status" : "success"
    }),201

@app.route("/liked-article",methods = ["POST"])
def liked_article():
    article = df[0]
    df = df[1:]
    liked_articles.append(article)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/disliked-article",methods = ["POST"])
def disliked_article():
    article = df[0]
    df = df[1:]
    disliked_articles.append(article)
    return jsonify({
        "status" : "success"
    }),201 

if __name__ == "__main__":
    app.run()












