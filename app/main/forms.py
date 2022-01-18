from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    message = StringField('What do you want to display?', validators=[DataRequired()])
    submit = SubmitField('Submit')
