# Praise Ye The Lord

# Import libraries
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class AdminForm(FlaskForm):
    username = StringField("username", validators=[DataRequired])
    password = PasswordField("password", validators=[DataRequired])