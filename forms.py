from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    usuario = StringField("Nombre de usuario", validators=[InputRequired(), Length(min=4, max=150)])
    passw = PasswordField("Contraseña", validators=[InputRequired(), Length(min=4, max=150)])
    submit = SubmitField("Registrar")

class LoginForm(FlaskForm):
    usuario = StringField("Usuario", validators=[InputRequired()])
    passw = PasswordField("Contraseña", validators=[InputRequired()])
    submit = SubmitField("Entrar")
