from crypt import methods
from flask import Flask,jsonify,request
import csv

all_movies=[]
with open('movies.csv') as f:
    file_name=csv.reader(f)
    data=list(file_name)
    all_movies=data[1:]

liked_list=[]
not_watched_list=[]
not_liked_list=[]

app=Flask(__name__)

@app.route('/get-movie')
def get_movie():
    return jsonify({
        'data':all_movies[0],
        'status':'success'
    })

@app.route('/liked-movie',methods('POST'))
def liked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_list.append(movie)
    return jsonify({
        'status':'success'
    }),201

@app.route('/not-liked-movie',methods('POST'))
def not_liked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_liked_list.append(movie)
    return jsonify({
        'status':'success'
    }),201

@app.route('/not-watched-movie',methods('POST'))
def not_watched_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_watched_list.append(movie)
    return jsonify({
        'status':'success'
    }),201


if __name__ == '__main__':
    app.run()