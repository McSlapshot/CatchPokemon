from app import app
from flask import render_template
from flask_login import current_user
from .models import User

@app.route('/')
def homePage():
    users = User.query.all()

    team_set = set()
    if current_user.is_authenticated:
        my_team = current_user.trainer.all()
        print(my_team)
        for u in my_team:
            team_set.add(u.id)
        
        for u in users:
            if u.id in team_set:
                u.flag = True

    return render_template('index.html', users=users)

@app.route('/login')
def loginPage():
    return render_template('login.html')