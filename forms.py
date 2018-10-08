# Define Web Form
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DecimalField, SelectField, FloatField
from wtforms.validators import DataRequired

class UsersForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  first_name = StringField('First Name', validators=[DataRequired()])
  last_name = StringField('Last Name', validators=[DataRequired()])
  prog_lang = SelectField('Programming Language', validators=[DataRequired()], choices=[('cpp', 'C++'), ('java', 'Java'), ('js', 'JavaScript'), ('php', 'Php'), ('py', 'Python'), ('other', 'Other')])
  experience_yr = FloatField('Years of Experience', validators=[DataRequired()])
  age = IntegerField('Age', validators=[DataRequired()])
  hw1_hrs = FloatField('Hours Spent on HW 1', validators=[DataRequired()])
  add_u = SubmitField('Add')
