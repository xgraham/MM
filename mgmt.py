from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from sqlalchemy import select, func, insert

from app import db, UserModel
from models import MovieModel, MovieGenre, Genre, UserMovieStatus, UserMatch

mgmt = Blueprint('mgmt', __name__)


@mgmt.route('/manage')
def manage():
    movies = get_movies()

    matches = get_matches()
    return render_template('auth/manage.html', movies=movies, matches = matches)


@mgmt.route('/add', methods=['POST'])
def add_post():
    other_email = request.form.get('email')
    user = UserModel.query.filter_by(
        email=other_email).first()
    if user:
        new_mate = UserMatch(user=current_user.user_id, other_user=user.user_id)
        db.session.add(new_mate)
        db.session.commit()
    else:
        flash('Email address doesn\'t exist')
        return redirect(url_for('mgmt.add'))
    movies = get_movies()
    matches = get_matches()
    return render_template("auth/manage.html", movies=movies, matches=matches)


@mgmt.route('/add')
def add():
    return render_template('auth/add.html')


def status_to_text(status):
    if status == 1:
        return 'liked'
    elif status == 2:
        return "disliked"
    elif status == 3:
        return "seen"


def get_movies():
    movies = [{}]
    usermovies = UserMovieStatus.query.filter_by(user_id=current_user.user_id).all()

    for movie in usermovies:
        current_movie = MovieModel.query.filter_by(movie_id=movie.movie_id).first()
        status = status_to_text(int(movie.status_id))
        movies.append({"title": current_movie.title, "status": status})
    return movies


def get_matches():
    matches = [{}]
    mates = UserMatch.query.filter_by(user_id=current_user.user_id).all()
    for match in mates:
        mate = UserModel.query.filter_by(user_id=match.otheruser_id).first()
        email = mate.email
        matches.append({"email":email})

    return matches
