from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from .forms import MyQuestionForm
from .models import Questions

def search(request):

    if request.method == "POST":
        form = MyQuestionForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('thanks/')

    else:

        form = MyQuestionForm()

        return render(request, "questionQuery/question.html", {'form': form})

def answer(request):
        return HttpResponse(Questions.objects.last())
