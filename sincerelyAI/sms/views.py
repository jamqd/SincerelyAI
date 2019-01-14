from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

import tensorflow as tf
from keras.models import load_model
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow_hub as hub
import numpy as np
import os
import json
from keras import backend as K

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    que = [(request.POST.__getitem__('Body'))]

    resp = MessagingResponse()

    msg = resp.message("Input received")

    m_out(request.POST.__getitem__('From'), "Input received")

    os.environ["TFHUB_CACHE_DIR"] = '/Users/joshuayoung/Desktop/TFlow'
    module_url = "https://tfhub.dev/google/universal-sentence-encoder/2"
    embed = hub.Module(module_url)
    print("downloaded USE TF hub module")

    m_out(request.POST.__getitem__('From'), "Processing")

    with tf.Session() as sess:
        sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
        # create question embeddings
        question_embeddings = sess.run(embed(que))
        print("created question embeddings")

    model = load_model('/Users/joshuayoung/Desktop/SBHacksV/sincerelyAI/questionQuery/final.h5')
    sin = model.predict(question_embeddings)
    print(sin)
    K.clear_session()
    if sin >= 0.5:
        lForm = "Insincere."
    else:
        lForm = "Sincere."

    # Add a text message
    #msg = resp.message(lForm)

    # Add a picture message
    #msg.media("https://demo.twilio.com/owl.png")

    m_out(request.POST.__getitem__('From'), lForm)

    return HttpResponse(resp)


# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def m_out(phoneNumber, message):
# Your Account Sid and Auth Token from twilio.com/console
    #account_sid = AUTH_ID
    #auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=message,
                         from_='[+1][323][9974536]',
                         to=phoneNumber
                     )
    return
