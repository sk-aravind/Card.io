

# Part 1 - Data Preprocessing ############################################

# Importing the libraries
import numpy as np

import pandas as pd

# Importing the dataset
dataset = pd.read_csv('HeartDiseaseData.csv')
X = dataset.iloc[:, 0:13].values #index of columns in the independent (predictor) variables
y = dataset.iloc[:, 13:18].values #col 13 (what we are predicting)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
# test size=0.2 means 20% of total rows is test (8000 train, 2000 test)

# Feature Scaling - MUST scale for any NN model
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - Making the ANN! ##############################################

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential # used to initialize NN
from keras.layers import Dense # model to create different layers in NN
from keras.models import load_model

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 9, kernel_initializer = 'uniform', activation = 'relu', input_dim = 13))
# dense helps to put an initial weight (needs to start somewhere)
# add (layer) will add a layer
# 6 nodes in the hidden layer (tip: input nodes + output nodes /2), and tells next layer no. of nodes to expect
# uniform is to randomly initialize the weights to a uniform distribution
# activation is the function you will use (relu is rectifier)
# input dim --> number of inputs from input layer

# Adding the second hidden layer
classifier.add(Dense(units = 9, kernel_initializer = 'uniform', activation = 'relu'))
# knows what inputs to expect because there is already an input layer created

# Adding the output layer
classifier.add(Dense(units = 5, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# using adam optimizer --> algorithm to use to find the optimal weights
# loss: need to have a loss function (which you are trying to minimize), binary crossentropy for binary output
                                     
# Fitting the ANN to the Training set and training the ANN
classifier.fit(X_train, y_train, batch_size = 15, epochs = 1000)
# fit(training set, ouput of training set, batch size, epochs)
# batch size: how many observations pass through before we update the weights
# epochs: number of times the whole training set goes through ANN

classifier.save("HF_Predict_model.h5")
# Part 3 - Making predictions and evaluating the model ############################

# Predicting the Test set results
y_pred = classifier.predict(X_test) # gives prediction for each observation in test set
# use higher threshold for sensitive info (like medicine)
# now in y_pred dataframe, it gives answer as true/false, rather than just probability


sample_patient = sc.transform(np.array([[54,1,4,168,350,0,2,167,1,2.8,2,2,7]]))
sample_pred = classifier.predict(sample_patient)
