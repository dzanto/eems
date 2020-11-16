from django import forms
from . import models


class DateTimeInput(forms.DateTimeInput):
    value = '2018-07-22'
    input_type = 'datetime-local'
    min = "2018-01-01"
    max = "2018-12-31"


class ClaimForm(forms.ModelForm):
    class Meta:
        model = models.Claim
        fields = '__all__'

        help_texts = {
            "claim_text": "Введите текст заявки",
        }

        labels = {
            'claim_text': 'Текст',
        }
        widgets = {
            'claim_text': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
            'pub_date': DateTimeInput(),
            'fix_date_time': DateTimeInput(),
            'report_text': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = '__all__'
