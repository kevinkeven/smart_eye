from django import forms
from django.forms import fields
from .models import Cam
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit, Row, Column, Field

class DirectionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            Field('turn_right', css_class='form-range'),
            Field('turn_left', css_class='form-range'),
        )