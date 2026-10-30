'''
in this file we create a model in a knn algorithm by using the Iris dataset
'''

#import all the librarys
import pandas as pd
import numpy as np
import matplotlib as plt
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
import pickle
import warnings
warnings.filterwarnings('ignore')

#take the breast_cancer dataset
df=pd.read_csv("IRIS - IRIS.csv") # paste the file name here



#to see all the column names

columm_names=df.columns

#in the dependent column is in the form of text so convert into a number

df['species']=df['species'].map(({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2})).astype(int)

#independent columns in a varilble capital X and dependent columns in y

X=df.iloc[ : , : -1]
y=df.iloc[ : , -1]

#now we split the data into a training and testing part

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


#give data to alg(KNN)

reg=KNeighborsClassifier(n_neighbors=3)#best k_value was 3

reg.fit(x_train,y_train)

#to find the best k_value

k_value=np.arange(3,50,2) #take odd values up to 50
test_accuracy_list=[]

for i in k_value:
    reg=KNeighborsClassifier(n_neighbors=i)
    reg.fit(x_train,y_train)
    ans_on_sun=reg.predict(x_test)
    test_accuracy_list.append(accuracy_score(y_test,ans_on_sun))

print(f"the best k_value was:{k_value[np.argmax(test_accuracy_list)]}")

#training performance

#to predict the values

train_prediction_values=reg.predict(x_train)

# to find the confusion_metrix training data
print(confusion_matrix(y_train,train_prediction_values))

#to find the accuracy_score training data
print(f"accuracy score of the training data was:{accuracy_score(y_train,train_prediction_values)}")

#to find the classification_report in training data

print(classification_report(y_train,train_prediction_values))

print('=========================================')
#testing performance

#to predict the values in test

test_prediction_values=reg.predict(x_test)

#to find the confusion_metrix in the testing data

print(confusion_matrix(y_test,test_prediction_values))

#to find the accuracy score of testing data was

print(f"the testing accuracy was:{accuracy_score(y_test,test_prediction_values)}")

#to find the classification report for the testing data was

print(f"{classification_report(y_test,test_prediction_values)}")

#predict own data point

big_leaf_length=0.3
big_leaf_width=0.5
small_leaf_length=0.2
small_leaf_width=0.1

result=reg.predict([[big_leaf_length,big_leaf_width,small_leaf_length,small_leaf_width]])[0]


if result==0:
  print(f"The Tree was : Setosa")
elif result==1:
  print(f"The Tree was : versicolor")
else:
  print(f"The Tree was : virginica")


#save the model
import pickle
with open("KNN_Multi_level_Classification_Model.pkl","wb") as f:
    pickle.dump(reg,f)
#load the model

with open("KNN_Multi_level_Classification_Model.pkl","rb") as p:
    m=pickle.load(p)

#check the model is predicted or not
big_leaf_length=5.6
big_leaf_width=2.5
small_leaf_length=7.1
small_leaf_width=3.9
model_check=m.predict([[big_leaf_length,big_leaf_width,small_leaf_length,small_leaf_width]])[0]


if model_check==0:
   print(f"The Tree was : Setosa")
elif model_check==1:
   print(f"The Tree was : versicolor")
else:
  print(f"The Tree was : virginica")