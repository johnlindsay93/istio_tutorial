from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField


class QueryServices(FlaskForm):
    service1 = SubmitField('Service1')


