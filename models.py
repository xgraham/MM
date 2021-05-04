from sqlalchemy import ForeignKey
from flask_login import UserMixin

from app import db


class UserModel(UserMixin, db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.name}>"

    def get_id(self):
        return (self.user_id)


class MovieModel(db.Model):
    __tablename__ = 'movie'

    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String())
    summary = db.Column(db.String())
    date_added = db.Column(db.String())
    release_year = db.Column(db.String())
    runtime = db.Column(db.String())

    def __init__(self, title, summary, added, release_year, runtime):
        self.title = title
        self.summary = summary
        self.date_added = added
        self.release_year = release_year
        self.runtime = runtime

    def __repr__(self):
        return f"<Movie {self.title}>"

    def get_title(self):
        return self.title


class Genre(db.Model):
    __tablename__ = 'genre'

    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre = db.Column(db.String())

    def __init__(self, genre):
        self.genre = genre

    def __repr__(self):
        return f"<Genre {self.genre}"


class Status(db.Model):
    __tablename__ = "status"

    status_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String())

    def __init__(self, status):
        self.status = status


class MovieGenre(db.Model):
    __tablename__ = 'moviegenre'

    moviegenre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, ForeignKey('movie.movie_id'), nullable=False)
    genre_id = db.Column(db.Integer, ForeignKey('genre.genre_id'), nullable=False)

    def __init__(self, movieid, genreid):
        self.movie_id = movieid
        self.genre_id = genreid


class UserMovieStatus(db.Model):
    __tablename__ = 'usermoviestatus'

    usermoviestatus_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, ForeignKey('movie.movie_id'), nullable=False)
    status_id = db.Column(db.Integer, ForeignKey('status.status_id'), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'), nullable=False)

    def __init__(self, movie, status, user):
        self.movie_id = movie
        self.status_id = status
        self.user_id = user


class Password(db.Model):
    __tablename__ = 'password'

    pw_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String)
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'), nullable=False)

    def __init__(self, password, user):
        self.password = password
        self.user_id = user


class UserMatch(db.Model):
    __tablename__ = 'usermatch'
    usermatch_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'), nullable=False)
    otheruser_id = db.Column(db.Integer, ForeignKey('user.user_id'), nullable=False)

    def __init__(self,user,other_user):
        self.user_id=user
        self.otheruser_id = other_user
