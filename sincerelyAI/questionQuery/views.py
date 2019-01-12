from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions
from .forms import MyQuestionForm, LabelForm

#import tensorflow as tf
#import tensorflow_hub as hub
import json

@csrf_exempt
def search(request):

    if request.method == "POST":
        print("post request")
        # Import the Universal Sentence Encoder's TF Hub module
        #module_url = "https://tfhub.dev/google/universal-sentence-encoder/2"
        #embed = hub.Module(module_url)
        #print("downloaded USE TF hub module")

        form = MyQuestionForm(request.POST)
        
        if not request.POST.get('question_query'):
            print("yaa?")
            return HttpResponse(request.body.decode('utf-8'))
        

        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save() #save to this?

            que = [Questions.objects.last()]

            #with tf.Session() as sess:
            #    sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
                # create question embeddings
            #    question_embeddings = sess.run(embed(que))
            #    print("created question embeddings")


            lForm = que[0]#LabelForm(label_suffix=form.cleaned_data['question_query'])
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
