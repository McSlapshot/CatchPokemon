from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateTeam(FlaskForm):
    team_name = StringField('Team_Name', validators=[DataRequired()])
    img_url = StringField('Image', validators=[DataRequired()])
    caption = StringField('Caption')
    submit = SubmitField()