from django.forms import ModelForm
from django import forms
from .models import Questions

class MyQuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question_query', 'question_answer']

class LabelForm(forms.Form):
    answer = forms.CharField(label_suffix='yes')
