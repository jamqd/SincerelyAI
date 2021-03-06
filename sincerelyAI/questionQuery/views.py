from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions
from .forms import MyQuestionForm, LabelForm

import tensorflow as tf
from keras.models import load_model
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow_hub as hub
import numpy as np
import os
import json
from keras import backend as K

@csrf_exempt
def search(request):

    print("USE TF hub module download started")
    os.environ["TFHUB_CACHE_DIR"] = '/Users/johndang/tfhub'
    module_url = "https://tfhub.dev/google/universal-sentence-encoder/2"
    embed = hub.Module(module_url)
    print("downloaded USE TF hub module")

    if request.method == "POST":
        print("post request")

        form = MyQuestionForm(request.POST)

        if not request.POST.get('question_query'):
            print("yaa?")
            quchr = [request.body.decode('utf-8')]

            with tf.Session() as sess:
                sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
                # create question embeddings
                question_embeddings = sess.run(embed(quchr))
                print("created question embeddings")

            model = load_model('/Users/johndang/git/SBHacks/sincerelyAI/questionQuery/final.h5')
            lrep = ""
            sin = model.predict(question_embeddings)
            print(sin)
            K.clear_session()
            if sin >= 0.5:
                lrep = "We think that question was INSINCERE!"
            else:
                lrep = "We think that question was SINCERE!"

            return HttpResponse(lrep)



        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()

            que = [Questions.objects.last().question_query]

            with tf.Session() as sess:
                sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
                # create question embeddings
                question_embeddings = sess.run(embed(que))
                print("created question embeddings")

            model = load_model('/Users/johndang/git/SBHacks/sincerelyAI/questionQuery/final.h5')
            sin = model.predict(question_embeddings)
            print(sin)
            K.clear_session()
            if sin >= 0.5:
                lrep = "We think that question was INSINCERE!"
            else:
                lrep = "We think that question was SINCERE!"

            return render(request, "questionQuery/answer.html", {'lForm': lrep})

    else:

        form = MyQuestionForm()

    return render(request, "questionQuery/question.html", {'form': form})

def result(request):
    if request.method == "POST":
        form = MyQuestionForm()
        return render(request, "questionQuery/question.html", {'form': form})

    return HttpResponse(Questions.objects.last())

#def history(request):
#    query_results = Questions.objects.all()
#    return render(request, "questionQuery/history.html", {'history': query_results[:10]})
