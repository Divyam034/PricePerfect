# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:38:00 2021

@author: Divyam
"""

import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

cars_data = pd.read_csv('C:/Users/Divyam/nptelswayam/car_cleaned.csv' )
cars=cars_data.copy()
cars["fuel_type"] = cars["fuel_type"].astype("category")
cars["year"] = cars["year"].astype("int64")
print(cars.info())

final_dataset =cars[['selling_price',"year","mileage", "max_power", 'fuel_type',"km_driven"]]
print(final_dataset["fuel_type"].unique())
print(final_dataset.info())
#final_dataset.to_csv("car_cleaned1.csv", index = False)
final_dataset = pd.get_dummies(final_dataset, drop_first = True)

import seaborn as sns
sns.pairplot(final_dataset) #Its showing relation between each feature

import matplotlib.pyplot as plt
final_dataset.corr()
corrmat=final_dataset.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))

g=sns.heatmap(corrmat,annot=True,cmap="RdYlGn") #Its showing the correlation factor between each features in the datset


#The dependent and independent column devided as x and y
X = final_dataset.iloc[:,1:]
Y = final_dataset.iloc[:,0] 
Y = np.log(Y)
# Model parameters
rf = RandomForestRegressor(n_estimators = 100,max_features="auto",\
max_depth=100,min_samples_split=10,\
min_samples_leaf=4,random_state=1)
# Model
model_rf1=rf.fit(X,Y)
# Predicting model on test set
cars_predictions_rf1 = rf.predict(X)
# Computing MSE and RMSE
rf_mse1 = mean_squared_error(Y, cars_predictions_rf1)
rf_rmse1 = np.sqrt(rf_mse1)
print(rf_rmse1)
# R squared value
r2_rf_test1=model_rf1.score(X,Y)
#r2_rf_train1=model_rf1.score(X_train,y_train)
print(r2_rf_test1) #r2_rf_train1
print("RMSE value for test from Random Forest= %s"% rf_rmse1)
joblib.dump(model_rf1, "car_model")
