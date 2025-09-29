# forms.py
from django import forms

class BirthDateForm(forms.Form):
    birth_date = forms.DateField(label="Дата рождения", input_formats=['%Y-%m-%d'])