import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import keras
import os
import numpy as np

reg = 0.01

print("loading data")

embeddingsR = pd.read_csv("data/question_embeddings_full.csv")
embeddings = embeddingsR.values

labelsR = pd.read_csv("data/train.csv")
labels = labelsR.values[:,2]

examples = 0
if(embeddings.shape[0] < labels.shape[0]):
    examples = embeddings.shape[0]
else:
    examples = labels.shape

embeddings = embeddings[:examples,:]
labels = labels[:examples]

combined = np.concatenate((embeddings, labels), axis=1)
np.random.shuffle(combined)

div1 = round(examples * 0.6)
div2 = round(examples * 0.8)

print("creating split datasets")
embeddings_train, labels_train = combined[:div1, :512], combined[:div1, 512]
embeddings_crossval, labels_crossval = combined[div1:div2, :512], combined[div1:div2, 512]
embeddings_test, labels_test = combined[div2:, :512], combined[div2:, 512]

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import regularizers

model = Sequential()
model.add(Dense(512, activation='relu', input_dim=512, kernel_regularizer=regularizer.l2(reg)))
model.add(Dense(1024, activation='relu', kernel_regularizer=regularizer.l2(reg)))
model.add(Dense(256, activation='relu', kernel_regularizer=regularizer.l2(reg)))
model.add(Dense(1, activation='sigmoid', kernel_regularizer=regularizer.l2(reg)))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics = ['accuracy'])



print(model.summary())

#callback functions
filepath="weights-improvement-{epoch:02d}-{val_acc:.2f}.h5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

# Train the model, iterating on the data in batches of 32 samples
model.fit(embeddings_train, labels_train, validation_data=(embeddings_crossval, labels_crossval), epochs=10, batch_size=32, callbacks=callbacks_list, verbose=1)

model.save("final.h5")

#metrics definitions
def precision(y_true, y_pred):
    true_positives = np.sum(y_true * y_pred)
    predicted_positives = np.sum(y_pred)
    precision = true_positives / predicted_positives
    return precision


def recall(y_true, y_pred):
    true_positives = np.sum(y_true * y_pred)
    possible_positives = np.sum(y_true)
    recall = true_positives / possible_positives
    return recall


def fmeasure(y_true, y_pred):
    return 2 * precision(y_true, y_pred) * recall(y_true, y_pred)/ (precision(y_true, y_pred) + recall(y_true, y_pred))

#crossvalidation set
print("validation: ")
predictions = (model.predict(embeddings_crossval) >= 0.5)[:,0]
print("precision: ")
print(precision(labels_crossval, predictions))
print("recall: ")
print(recall(labels_crossval, predictions))
print("f1 score: ")
print(fmeasure(labels_crossval, predictions))

#test set
print("test set: ")
predictions = (model.predict(embeddings_test) >= 0.5)[:,0]
print("precision: ")
print(precision(labels_test, predictions))
print("recall: ")
print(recall(labels_test, predictions))
print("f1 score: ")
print(fmeasure(labels_test, predictions))