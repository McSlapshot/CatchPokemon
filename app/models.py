from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

team = db.Table(
    'team',
    db.Column('trainer_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('pokeball_id', db.Integer, db.ForeignKey('pokemon.id'), nullable=False)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship("Post", backref='author', lazy=True)

    trainer = db.relationship("User",
        primaryjoin = (team.c.trainer_id==id),
        secondaryjoin = (team.c.pokeball_id==id),
        secondary = team,
        backref= db.backref('team', lazy='dynamic'),
        lazy='dynamic'
    )

    # pokemon = db.relationship("Pokemon", backref='author', lazy=True)
    # pokemons = db.relationship("User",
    #     primaryjoin = (team.c.user_id==id),
    #     secondaryjoin = (team.c.pokemon_id==id),
    #     secondary = team,
    #     backref= db.backref('team', lazy='dynamic'),
    #     lazy='dynamic'
    # )

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    def saveChanges(self):
        db.session.commit()

    # def addToTeam(self, user):
    #     self.pokemons.append(user)
    #     db.session.commit()

    # def removeFromTeam(self, user):
    #     self.pokemons.remove(user)
    #     db.session.commit()

    def addTeam(self, user):
        self.trainer.append(user)
        db.session.commit()

    def removeTeam(self,user):
        self.trainer.remove(user)
        db.session.commit()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    img_url = db.Column(db.String)
    caption = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, img_url, caption, user_id):
        self.title = title
        self.img_url = img_url
        self.caption = caption
        self.user_id = user_id

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    def saveChanges(self):
        db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    ability = db.Column(db.String(150), nullable=False)
    img_url = db.Column(db.String)
    base_exp = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, ability, img_url, base_exp, hp, attack, defense, speed, user_id):
        self.name = name
        self.ability = ability
        self.img_url = img_url
        self.base_exp = base_exp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.user_id = user_id

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

