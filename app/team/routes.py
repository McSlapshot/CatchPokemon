from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required, current_user
from app.models  import Team
from .forms import CreateTeam

team = Blueprint('team', __name__, template_folder='team_templates')

@team.route('/teams/create_team', methods=["GET", "POST"])
@login_required
def createTeam():
    form = CreateTeam()
    if request.method == "POST":
        if form.validate():
            team_name = form.team_name.data
            img_url = form.img_url.data
            caption = form.caption.data

            team = Team(team_name, img_url, caption, current_user.id)

            team.saveToDB()

            return redirect(url_for('homePage'))

    return render_template('create_team.html', form=form)

@team.route('/teams')
def viewTeams():
    teams = Team.query.order_by(Team.date_created).all()[::-1]
    return render_template('team.html', teams=teams)