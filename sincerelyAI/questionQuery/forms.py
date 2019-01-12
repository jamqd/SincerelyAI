from django.forms import ModelForm
from .models import Questions

class MyQuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question_query', 'question_answer']
