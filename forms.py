from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class JsonStringInput(FlaskForm):
	json  = StringField("Json", validators = [DataRequired()] )
	button = SubmitField("Convert")
