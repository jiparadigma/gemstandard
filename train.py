# Save Model Using Pickle
import pandas as pd
from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle



url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(url, names=names)
dataframe.to_csv("validation.data", index = False)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
# Fit the model on 33%
model = LogisticRegression()
model.fit(X_train, Y_train)
# save the model to disk
filename = 'model.pkl'
pickle.dump(model, open(filename, 'wb'))

# some time later...

