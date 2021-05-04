from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from sqlalchemy import select, func, insert
import movie_requester
from app import db
from models import MovieModel, MovieGenre, Genre, UserMovieStatus

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/swipe')
@login_required
def swipe():
    movie = MovieModel.query
    movie = movie.order_by(func.random())
    movie = movie.first()
    print(movie)
    moviegenre = MovieGenre.query.filter_by(movie_id=movie.movie_id)
    genres = []
    for item in moviegenre:
        genre = Genre.query.filter_by(genre_id=item.genre_id)
        genres.append(genre.first().genre)
    print(genres)
    img_url = movie_requester.get_tmdb_img(movie.title, movie.release_year)
    return render_template('swipe.html', movie=movie, genres=genres,img_url = img_url)



@main.route('/like')
@login_required
def like():
    movie_id = request.args.get('id')
    print(movie_id)

    set_status(movie_id,1)
    return redirect(url_for('main.swipe'))

@main.route('/dislike')
@login_required
def dislike():
    movie_id = request.args.get('id')

    set_status(movie_id,2)
    return redirect(url_for('main.swipe'))

@main.route('/seen')
@login_required
def seen():
    movie_id = request.args.get('id')
    set_status(movie_id,3)
    return redirect(url_for('main.swipe'))


def set_status(movie,status):
    movieuserstatus = UserMovieStatus(movie,status,current_user.user_id)
    db.session.add(movieuserstatus)
    db.session.commit()

@main.route('/profile')
@login_required
def profile():

    return render_template('profile.html', name=current_user.name)