
from flask import Flask, render_template, session, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy

################################################################################

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'adm36'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_movies.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff

#from db import db
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

#########
######### Everything above this line is important/useful setup, not problem-solving.
#########


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    genre = db.Column(db.String(64))
    director = db.Column(db.String(64))
    release = db.Column(db.String(64))
    mpaa = db.Column(db.String(64))
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))

    def __repr__(self):
        return "{} has been added to your database".format(self.title)

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Director')

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)

####################################################################


def get_or_create_director(director_name):
    director = Director.query.filter_by(name=director_name).first()
    if director:
        return director
    else:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
        return director

#####################################################################
## Main route
@app.route('/')
def index():
    movies = Movie.query.all()
    num_movies = len(movies)
    return render_template('index.html', num_movies=num_movies)

@app.route('/movie/new/<title>/<director>/<genre>/')
def new_song(title, director, genre):
    if Movie.query.filter_by(title=title).first(): # if there is a movie by that title
        return "That movie already exists! Go back to the main app!"
    else:
        director = get_or_create_director(director)
        movie = Movie(title=title, director_id=director.id,genre=genre)
        session.add(movie)
        session.commit()
        return "New movie: {} by {}.".format(movie.title, director.name)

@app.route('/all_movies')
def see_all():
    all_movies = [] # Will be be tuple list of title, genre
    movies = Movie.query.all()
    for m in movies:
        director = Director.query.filter_by(id=m.director_id).first() # get just one artist instance
        all_movies.append((m.title,director.name, m.genre)) # get list of songs with info to easily access [not the only way to do this]
    return render_template('all_movies.html',all_movies=all_movies) # check out template to see what it's doing with what we're sending!

@app.route('/all_directors')
def see_all_directors():
    directors = Director.query.all()
    names = []
    for d in directors:
        num_movies = len(Movie.query.filter_by(director_id=d.id).all())
        newtup = (d.name,num_movies)
        names.append(newtup) # names will be a list of tuples
    return render_template('all_directors.html',director_names=names)


if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    app.run() # run with this: python main_app.py runserver
