from django import forms

class NameForm(forms.Form):
    meme_no = forms.CharField(label='Your name', max_length=100)
    field_1 = forms.CharField(label='Your name', max_length=100)
    field_2 = forms.CharField(label='Your name', max_length=100)
    field_3 = forms.CharField(label='Your name', max_length=100)
    field_4 = forms.CharField(label='Your name', max_length=100)
