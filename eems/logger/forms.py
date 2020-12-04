from django import forms
from . import models
from dal import autocomplete


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
            'claim_text': forms.Textarea(attrs={'cols': 40, 'rows': 6}),
            'pub_date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
            'address': autocomplete.ModelSelect2(url='logger:address-autocomplete'),
            'fix_date_time': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local',}),
            'report_text': forms.Textarea(attrs={'cols': 40, 'rows': 6}),
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
            'task_text': forms.Textarea(attrs={'cols': 40, 'rows': 6}),
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
            'fix_date': forms.DateInput(attrs={'type': 'date'}),
            'report_text': forms.Textarea(attrs={'cols': 40, 'rows': 6}),
        }
