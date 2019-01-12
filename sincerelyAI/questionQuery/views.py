from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions
from .forms import MyQuestionForm, LabelForm

def search(request):

    if request.method == "POST":
        form = MyQuestionForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            qu = Questions.objects.last()
            lForm = Questions.objects.last()#LabelForm(label_suffix=form.cleaned_data['question_query'])
            return render(request, "questionQuery/answer.html", {'lForm': lForm})
            #print(form.cleaned_data['question_query']) #'answer':answer
            #return HttpResponseRedirect('/result/')
            #return redirect('/')

    else:

        form = MyQuestionForm()

    return render(request, "questionQuery/question.html", {'form': form})

def result(request):
    if request.method == "POST":
        form = MyQuestionForm()
        return render(request, "questionQuery/question.html", {'form': form})

    return HttpResponse(Questions.objects.last())
