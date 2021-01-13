from django import forms
from . import models
from dal import autocomplete
from django.core.exceptions import NON_FIELD_ERRORS


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


class OtherClaimForm(forms.ModelForm):

    class Meta:
        model = models.Claim
        exclude = ['author', 'elevator']
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
            'fix_date_time': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local',}),
            'report_text': forms.Textarea(attrs={'cols': 40, 'rows': 6}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = '__all__'
        help_texts = {
            "city": "Необязательное поле",
            'entrance': 'Необязательное поле',
            'floor': 'Необязательное поле',
            'apartment': 'Необязательное поле',
        }


class ElevatorForm(forms.ModelForm):
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     address = cleaned_data['address']
    #     if address and models.Elevator.objects.filter(address=address).exists():
    #         raise forms.ValidationError('Лифт с таким адресом уже существует')
    #     return cleaned_data

    class Meta:
        model = models.Elevator
        fields = ['address', 'note']
        widgets = {
            'address': autocomplete.ModelSelect2(url='logger:address-autocomplete'),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
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
    readonly_group = 'Электромеханики'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        user_groups = self.user.groups.all()
        super().__init__(*args, **kwargs)
        if user_groups.filter(name=self.readonly_group).exists():
            for field in self.readonly_fields:
                self.fields[field].widget.attrs['disabled'] = True

    def clean(self):
        cleaned_data = super().clean()
        user_groups = self.user.groups.all()
        if user_groups.filter(name=self.readonly_group).exists():
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

