from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Beneficiaries
from .choices import *


class DateInput(forms.DateInput):
    input_type = 'date'


class BeneficiariesForm(forms.ModelForm):
    surname = forms.CharField(label='Surname', max_length=200, required=True,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Surname'}
                            ))
    given_name = forms.CharField(label='Given Name', max_length=200, required=False,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Given Name'}
                             ))
    sex = forms.ChoiceField(choices=SEX_CHOICES, required=True)
    date_of_birth = forms.DateField(widget=DateInput(attrs={
            'class': 'form-control datetimepicker-input'}))
    place_of_birth = CountryField().formfield()
    height = forms.IntegerField(label='Height',
                                   required=True,
                                   widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'height'
                                                                   }
                                                            )
                                   )
    partner = forms.ChoiceField(choices=PARTNER_CHOICES, required=True)
    children = forms.BooleanField(label='Children',
                                         required=True,
                                         widget=forms.CheckboxInput(
                                             attrs={'class': 'form-control', 'placeholder': 'Children'})
                                         )
    number_children = forms.IntegerField(label='number children',
                                   required=True,
                                   widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'height'
                                                                   }
                                                            )
                                   )

    class Meta:
        model = Beneficiaries
        fields = [
            'surname',
            'given_name',
            'sex',
            'date_of_birth',
            'place_of_birth',
            'height',
            'partner',
            'children',
            'number_children',
        ]