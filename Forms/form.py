from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

class BasicForm(FlaskForm):
    desktop_btn = SubmitField("Desktop View")
    mobile_btn = StringField("Mobile View")