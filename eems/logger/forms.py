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
        # 'pub_date',
        'region',
        # 'elevator',
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        user_groups = self.user.groups.all()
        super().__init__(*args, **kwargs)
        # for field in self.readonly:
        #     self.fields[field].widget.attrs['disabled'] = True
        if user_groups.filter(name='Электромеханики').exists():
            for field in self.readonly_fields:
                self.fields[field].widget.attrs['disabled'] = True
            # self.fields['task_text'].widget.attrs['disabled'] = 'disabled'

    # def clean(self):
    #     cleaned_data = super().clean()
    #     for field in self.fields:
    #         cleaned_data[field] = getattr(self.instance, field)
    #     return cleaned_data

    def clean(self):
        cleaned_data = super().clean()
        user_groups = self.user.groups.all()
        if user_groups.filter(name='Электромеханики').exists():
            for field in self.readonly_fields:
                cleaned_data[field] = getattr(self.instance, field)
        return cleaned_data

    # def clean_task_text(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance:
    #         return instance.task_text
    #     else:
    #         return self.cleaned_data.get('task_text', None)
    #
    # def clean_elevator(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance:
    #         try:
    #         return instance.elevator
    #     else:
    #         return self.cleaned_data.get('elevator', None)

    class Meta:
        model = models.Task
        fields = '__all__'
        exclude = ['author']
        widgets = {
            'task_text': forms.Textarea(attrs={'cols': 40, 'rows': 6}),
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
            'order_date': forms.DateInput(attrs={'type': 'date'}),
            'fix_date': forms.DateInput(attrs={'type': 'date'}),
            'report_text': forms.Textarea(attrs={'cols': 40, 'rows': 6}),
            'fixed': forms.CheckboxInput(),
        }
