# -*- coding: utf-8 -*-
"""AGS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xkkrr97VUOqy1MuJzrirByYDrhdhrDG-
"""

from google.colab import drive
drive.mount('/content/drive/', force_remount=True)

import pandas as pd
file_path = "/content/drive/My Drive/heart.csv"
df = pd.read_csv(file_path)
x = df[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']]
y = df['target']

sample_data = pd.DataFrame({
    'age': [35, 42, 55, 28, 60],  # Age in years
    'sex': [0, 1, 0, 1, 0],  # Gender (0 for female, 1 for male)
    'cp': [1, 3, 2, 0, 1],  # Chest pain type (0, 1, 2, 3)
    'trestbps': [125, 130, 140, 118, 122],  # Resting blood pressure in mm Hg
    'chol': [210, 240, 200, 185, 250],  # Serum cholesterol level in mg/dL
    'fbs': [1, 0, 0, 1, 1],  # Fasting blood sugar (0 for <120 mg/dL, 1 for >=120 mg/dL)
    'restecg': [0, 1, 2, 0, 1],  # Resting electrocardiographic results (0, 1, 2)
    'thalach': [175, 160, 175, 140, 130],  # Maximum heart rate achieved
    'exang': [1, 0, 1, 0, 1],  # Exercise-induced angina (0 for no, 1 for yes)
    'oldpeak': [2.0, 1.2, 0.8, 0.0, 1.5],  # ST depression induced by exercise relative to rest
    'slope': [2, 1, 3, 2, 1],  # Slope of the peak exercise ST segment (1, 2, 3)
    'ca': [0, 1, 2, 0, 1],  # Number of major vessels colored by fluoroscopy (0, 1, 2, 3)
    'thal': [3, 2, 1, 3, 2]  # Thalassemia (1, 2, 3)
})

#Decision Tree
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(x,y)
print(classifier.predict(sample_data))

#Random Forest
from sklearn.ensemble import RandomForestRegressor
RandomForestRegModel = RandomForestRegressor()
RandomForestRegModel.fit(x,y)
print(RandomForestRegModel.predict(sample_data))

#KNN
from sklearn.neighbors import KNeighborsClassifier
classifier= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2 )
classifier.fit(x,y)
print(classifier.predict(sample_data))

#SVM
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(x,y)
print(classifier.predict(sample_data))

#Naive Bayes
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=22)
model=GaussianNB()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(y_pred)
print(model.score(x_test,y_test))

#Logistic Regression
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(y_pred)

import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load and preprocess your Heart Attack dataset

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Build a deep neural network
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(13,), kernel_initializer='he_uniform'),
    keras.layers.Dense(64, activation='relu', kernel_initializer='he_uniform'),
    keras.layers.Dense(64, activation='relu', kernel_initializer='he_uniform'),
    keras.layers.Dense(1, activation='sigmoid')
])
# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model with a specified number of epochs
model.fit(X_train, y_train, epochs=100, batch_size=64, verbose=1)

# Make predictions
y_pred_dl = model.predict(X_test)
y_pred_dl = (y_pred_dl > 0.5).astype(int)

# Calculate accuracy
accuracy_dl = accuracy_score(y_test, y_pred_dl)
print("Deep Learning (DNN) Accuracy:", accuracy_dl)