# Sincereley, AI

Created by:  John Dang, Bill Liu, Joshua Young, and Justin Shao


## Introduction

Sincerley, AI is a deep learning project with the goal of identifying insincere text. The model is trained on [this](https://www.kaggle.com/c/quora-insincere-questions-classification) dataset from Quora containing over 1.3 million data samples of sincere and insincere text. We used transfer learning in order to train our model based on a [research paper](https://arxiv.org/abs/1803.11175) released by Google AI Research in March 2018.


## Running the Demo

![Website Landing Page](webapp.png)

To create conda environment run the following command from the repo directory. 

`conda create --name quora --file requirements.txt`


To activate environment run 
`source activate quora`

**Note:** Users running the demo on a machine with a cuda enabled (Nvidia) GPU should run

`conda install tensorflow-gpu`

for significantly faster inference time.

From the sincerelyAI directory run

`python manage.py runserver`

to run the web app.
