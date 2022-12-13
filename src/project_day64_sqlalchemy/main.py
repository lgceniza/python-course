from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests

API_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
API_DETAILS_URL = 'https://api.themoviedb.org/3/movie/{id}'
API_IMAGE_URL = 'https://image.tmdb.org/t/p/original{img_url}'
API_KEY = 'fd614970fec1a4e4a0d3e9362d44ff83'

class AddMovieForm(FlaskForm):
  title = StringField('Movie Title', validators=[DataRequired()])
  submit = SubmitField('Add Movie')

class RateMovieForm(FlaskForm):
  rating = FloatField('Your Rating Out of 10:', validators=[DataRequired(), NumberRange(0,10)])
  review = StringField('Your Review:', validators=[DataRequired()])
  submit = SubmitField('Done')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), nullable=False)
  year = db.Column(db.Integer, nullable=False)
  description = db.Column(db.String(250), nullable=False)
  rating = db.Column(db.Float, nullable=True)
  ranking = db.Column(db.Integer, nullable=True)
  review = db.Column(db.String(250), nullable=True)
  img_url = db.Column(db.String(100), nullable=False)

# with app.app_context():
#   db.create_all()

@app.route('/')
def home():
  all_movies = Movie.query.order_by(Movie.rating.desc()).all()
  for i, movie in enumerate(all_movies):
    movie.ranking = i + 1
  return render_template('index.html', movies=all_movies)

@app.route('/add', methods=['GET','POST'])
def add():
  form = AddMovieForm()
  if form.validate_on_submit():
    title = form.title.data
    results = requests.get(API_SEARCH_URL, params={'api_key': API_KEY, 'query': title}).json()['results']
    return render_template('select.html', movies=results)
  return render_template('add.html', form=form)

@app.route('/select')
def select():
  movie_id = request.args.get('id')
  movie_data = requests.get(API_DETAILS_URL.format(id=movie_id),params={'api_key': API_KEY}).json()
  movie = Movie(
    title=movie_data['title'],
    year=movie_data['release_date'][:4],
    description=movie_data['overview'],
    img_url=API_IMAGE_URL.format(img_url=movie_data['poster_path'])
  )
  db.session.add(movie)
  db.session.commit()
  return redirect(url_for('home'))

@app.route('/edit', methods=['GET','POST'])
def edit():
  form = RateMovieForm()
  movie = Movie.query.get(request.args.get("id"))
  if form.validate_on_submit():
    movie.rating = float(form.rating.data)
    movie.review = form.review.data
    db.session.commit()
    return redirect(url_for('home'))
  return render_template('edit.html', movie=movie, form=form)

@app.route('/delete')
def delete():
  movie = Movie.query.get(request.args.get("id"))
  db.session.delete(movie)
  db.session.commit()
  return redirect(url_for('home'))


if __name__ == '__main__':
  app.run(debug=True)
