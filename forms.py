from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField("Nombre de usuario", validators=[InputRequired(), Length(min=4, max=150)])
    password = PasswordField("Contraseña", validators=[InputRequired(), Length(min=4, max=150)])
    submit = SubmitField("Registrar")

class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[InputRequired()])
    password = PasswordField("Contraseña", validators=[InputRequired()])
    submit = SubmitField("Entrar")
