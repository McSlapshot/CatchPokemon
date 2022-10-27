from app import app
from flask import render_template
from flask_login import current_user
from .models import User

@app.route('/')
def homePage():
    users = User.query.all()

    team_set = dict()
    for u in users:
        my_team = u.my_team.all()
        print(my_team)
        team_set[u.username] = my_team
        # for u in my_team:
        #     team_set.add(u.id)
        
        # for u in users:
        #     if u.id in team_set:
        #         u.flag = True

    return render_template('index.html', team_set=team_set)

@app.route('/login')
def loginPage():
    return render_template('login.html')