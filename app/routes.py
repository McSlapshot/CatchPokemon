from app import app
from flask import render_template
from flask_login import current_user
from .models import User, Pokedex, team

@app.route('/')
def homePage():
    users = User.query.all()

    team_set = set()
    if current_user.is_authenticated:
        my_team = team.trainer.all()
        print(my_team)
        for u in my_team:
            team_set.add(u.id)
        
        for u in users:
            if u.id in team_set:
                u.flag = True

    #trying to copy how I called each individual user but having trouble 
    
    # pokemon = Pokedex.query.get(current_user)
    # pokeball = set()
    # if pokemon :
    #     p = Pokedex.query.filter_by(pokemon_id=pokemon.id).first()
    
    return render_template('index.html', users=users)

@app.route('/login')
def loginPage():
    return render_template('login.html')

