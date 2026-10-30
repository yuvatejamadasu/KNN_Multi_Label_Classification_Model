'''
this file is a development file
we write a oops code for knn multi label classification algorithm
'''

#import all the librarys

import numpy as np
import pandas as pd
import matplotlib as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
import warnings
warnings.filterwarnings('ignore')
import pickle
import sys


#create a class
class KNN:
    def __init__(self,path):
        #take the dataset
        self.df=pd.read_csv(path)
        #in the dependent column has a data is in the form of text so convert into a number
        self.df['species']=self.df['species'].map({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2}).astype(int)
        self.X=self.df.iloc[ : , : -1]
        self.y=self.df.iloc[ : , -1]
        #now we split the data into a training part and testing part
        self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.X,self.y,test_size=0.2,random_state=42)

        #giv data to the algorithm(KNN)
        self.reg=KNeighborsClassifier()
        self.reg.fit(self.x_train,self.y_train)

    #Training data
    def training(self):

        try:

                #to predict the values
                self.train_predict=self.reg.predict(self.x_train)

                #to find the confusion_metrix of the training data
                print(f"the confusion_matrix in the training data was:")
                print(confusion_matrix(self.y_train,self.train_predict))

                #to find the accuracy_score  of the training data
                print(f"the accuracy_score in the training data was:")
                print(accuracy_score(self.y_train,self.train_predict))

                #to find the classification_report of the training data
                print(f"the classification_report in the training data was:")
                print(classification_report(self.y_train,self.train_predict))

        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"the error line was : {er_line} error type was : {er_ty} error msg was : {er_msg}")

    #Testing data performance

    def testing(self):

        try:


                #to predict the values
                 self.test_predict=self.reg.predict(self.x_test)

                #to find the confusion_matrix
                 print(f"the confusin_metrix in the testing was:")
                 print(confusion_matrix(self.y_test,self.test_predict))

                #to find the accuracy_score was
                 print(f"the accuracy_score in the testing was:")
                 print(accuracy_score(self.y_test, self.test_predict))

                #to find the classification-report
                 print(f"the classification_report in the testing was:")
                 print(classification_report(self.y_test,self.test_predict))

        except Exception as e:

            er_ty, er_msg, er_line = sys.exc_info()
            print(f"the error line was : {er_line} error type was : {er_ty} error msg was : {er_msg}")

    #save the model
    def saving(self):
        try:
            with open("KNN_Multi_level_Classification_Model.pkl","wb") as f:
                pickle.dump(self.reg,f)

             #load the model
            with open("KNN_Multi_level_Classification_Model.pkl","rb") as p:
                self.m=pickle.load(p)

            #predict the loaded file
            result=self.m.predict([[5.6,3.6,7.8,3.4]])[0]
            print(result)

        except Exception as e:
            er_ty,er_msg,er_line=sys.exc_info()
            print(f"the error line was : {er_line} error type was : {er_ty} error msg was : {er_msg}")


#creating the main method for the class and inside the main method we write objects for classes and methods
#the execution starts for the main method
if __name__=="__main__":
    dataset="IRIS - IRIS.csv"
    obj=KNN(dataset)
    obj.training()
    obj.testing()
    obj.saving()