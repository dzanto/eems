from django.forms.widgets import TextInput


class MyTextInput(TextInput):
    input_type = 'text'
    template_name = 'django/forms/widgets/text.html'