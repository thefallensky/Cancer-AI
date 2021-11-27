# -*- coding: utf-8 -*-
"""Cancer AI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MhCo__wbovAISW9ZH9fGMwrTBRbTbCP8
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

dataset = pd.read_csv('cancer.csv')

x = dataset.drop(columns = ['diagnosis(1=m, 0=b)'])
y = dataset['diagnosis(1=m, 0=b)']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
model = Sequential()
model.add(Dense(128, input_dim=30, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64,activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer = 'adam' , metrics = ['accuracy'])
model.summary()

model.fit(x_train,y_train)

model.evaluate(x_test,y_test)

import seaborn as sns   
y_pred = model.predict(x_test)   
y_pred = (y_pred > 0.5)   
# Making the Confusion Matrix:   
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
sns.heatmap(cm, annot = True)

predictions = model.predict(x_test)
prediction_classes = [
    1 if prob > 0.5 else 0 for prob in np.ravel(predictions)
]
print(prediction_classes)
len(prediction_classes)

