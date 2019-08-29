from model import predict
import pandas as pd
from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.metrics import mean_squared_error



# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv('validation.data')
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)


Y_pred = predict(X_test)
mse = mean_squared_error(Y_test,Y_pred)
print("MSE: ", mse)
assert round(mse,2) == 0.24, "ERROR: model does not behave as expected. check the file validation.data"
print("Model test OK")