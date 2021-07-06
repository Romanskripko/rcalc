from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FileField


class CalcData(FlaskForm):
    rtype = SelectField(label='Regression coefficient', default=2, choices=[1, 2, 3, 4])
    table = FileField(label='Your excel file (16 mb max, xlsx only)')
    solve = SubmitField("Solve")
