import numpy as np 
import pandas as pd 

df = pd.read_csv("placement.csv")
print(df.head(2))

x = df.drop(columns = ['placed'])
y = df['placed'] 

from sklearn.model_selection import train_test_split 

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2 , random_state = 42)

# print(x_train.head(2))

from sklearn.linear_model import LogisticRegression 
lr = LogisticRegression() 
lr.fit(x_train , y_train) 
y_pred = lr.predict(x_test) 

from sklearn.metrics import accuracy_score 

print(accuracy_score(y_test , y_pred))