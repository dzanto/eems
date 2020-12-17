from django import forms
from . import models
from dal import autocomplete
from django.contrib.auth.models import Group


class ClaimForm(forms.ModelForm):

    class Meta:
        model = models.Claim
        fields = '__all__'
        exclude = ['author', 'address']

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
            'worker': autocomplete.ModelSelect2(url='logger:user-autocomplete'),
            'elevator': autocomplete.ModelSelect2(url='logger:elevator-autocomplete'),
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
        widgets = {
            'address': autocomplete.ModelSelect2(url='logger:address-autocomplete'),
        }


class TaskForm(forms.ModelForm):
    readonly_fields = (
        'task_text',
        'pub_date',
        'region',
        'elevator',
        'order_date',
        'worker',
        'fix_date',
        'fixed',
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        user_groups = self.user.groups.all()
        super().__init__(*args, **kwargs)
        if user_groups.filter(name='Электромеханики').exists():
            for field in self.readonly_fields:
                self.fields[field].widget.attrs['disabled'] = True

    def clean(self):
        cleaned_data = super().clean()
        user_groups = self.user.groups.all()
        if user_groups.filter(name='Электромеханики').exists():
            for field in self.readonly_fields:
                cleaned_data[field] = getattr(self.instance, field)
        return cleaned_data

    class Meta:
        model = models.Task
        fields = '__all__'
        exclude = ['author']
        widgets = {
            'task_text': forms.Textarea(attrs={'cols': 40, 'rows': 6}),
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
            'order_date': forms.DateInput(attrs={'type': 'date'}),
            'fix_date': forms.DateInput(attrs={'type': 'date'}),
            'elevator': autocomplete.ModelSelect2(url='logger:elevator-autocomplete'),
            'report_text': forms.Textarea(attrs={'cols': 40, 'rows': 6}),
            'fixed': forms.CheckboxInput(),
        }

