from django import forms
from . import models


class ClaimForm(forms.ModelForm):
    class Meta:
        model = models.Claim
        fields = ['claim_text', 'pub_date', 'address']

        help_texts = {
            "claim_text": "Введите текст заявки",
        }

        labels = {
            'claim_text': 'Текст',
        }
        widgets = {
            'claim_text': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
            'pub_date': forms.SelectDateWidget,
        }
