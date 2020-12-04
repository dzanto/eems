from django import forms
from . import models
from dal import autocomplete


class DateInput(forms.DateInput):
    value = "2013-01-08"
    input_type = "date"


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
            'pub_date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local',}),
            'address': autocomplete.ModelSelect2(url='logger:address-autocomplete'),
            'fix_date_time': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local',}),
            'report_text': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = '__all__'


class ElevatorForm(forms.ModelForm):
    class Meta:
        model = models.Elevator
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'
        widgets = {
            'fix_date': forms.DateInput(attrs={'type': 'date'}),
        }
