from flask_login import current_user
from app import app
from flask import render_template, flash, redirect, url_for
from .models import User, Pokemon

@app.route('/')
def homePage():
    users = User.query.all()

    team_set = dict()
    for u in users:
        my_team = u.my_team.all()
        print(my_team)
        team_set[u.username] = my_team
      
    return render_template('index.html', team_set=team_set)

@app.route('/login')
def loginPage():
    return render_template('login.html')

# unsure how to go about the pokemon battle but trying things out
@app.route('/battle')
def battle():
    users = User.query.all()

    team_set = dict()
    for u in users:
        my_team = u.my_team.all()
        print(my_team)
        team_set[u.username] = my_team
      
    return render_template('battle.html', team_set=team_set)

@app.route('/battle/results')
def battleResults():
    # users = Pokemon.query.all()

    # team_set = dict()
    # for u in users:
    #     my_team = u.my_team.all()
    #     team_set[u.attack] = my_team
    #     if current_user.my_team > u.my_team:
            flash('pokemon trainer defeated!', 'success')
            return redirect(url_for('homePage'))