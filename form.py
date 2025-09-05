from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=18)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    passwords = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=10)])
    confirmpass = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('passwords')])
    submit = SubmitField("Sign Up")
