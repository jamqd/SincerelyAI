from django import forms

class SentenceForm(forms.Form):
    sentence = forms.CharField(label='sincere', max_length=200)