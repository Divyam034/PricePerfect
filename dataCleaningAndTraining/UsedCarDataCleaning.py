# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:02:30 2021

@author: Divyam
"""

import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

os.chdir("C:/Users/Divyam/nptelswayam")

car_original = pd.read_csv("Cardekho_Extract.csv", na_values=["Max Powernull bhp"])

car_data = car_original.copy()
not_needed = ["Source.Name", "web-scraper-order", "web-scraper-start-url",\
              "new-price","seats","engine"]

car_data = car_original.drop(not_needed, axis=1)
car_data = car_data.dropna(axis=0)
car_data['company'] = car_data['full_name'].str.split(' ').str[0]
#print(car_data.info())



"""
Quality Issues in DataSet

1- selling_price (Object->Float64)      Done
2- seller_type (Object->Category)       Done
3- km_driven (Object->Float64)          Done
4- owner_type (Object->Category)        Done
5- fuel_type (Object->Category)         Done
6- transmission_type (Object->Category) Done
7- mileage (Object->Float64)            Done
9- max_power (Object->Float64)          Done
"""


#print(car_data["selling_price"].unique())
car_data["selling_price"]= car_data["selling_price"].replace\
            ({" Lakh":"","\*":"","\,":""}, regex=True)

car_data["selling_price"] = car_data["selling_price"].astype("float64")

car_data["selling_price"] = 100000*car_data["selling_price"]

#car_data[""]
#print(car_data["seller_type"])
car_data["seller_type"] = car_data["seller_type"].astype("category")


#print(car_data["km_driven"].unique())
car_data["km_driven"] = car_data["km_driven"].replace({" kms":"",",":""},\
                                                      regex=True)
car_data["km_driven"] = car_data["km_driven"].astype("float64")


#print(car_data["owner_type"].unique())
car_data["owner_type"] = car_data["owner_type"].astype("category")


#print(car_data["fuel_type"].unique())
car_data["fuel_type"] = car_data["fuel_type"].astype("category")
car_data["fuel_type"] = car_data["fuel_type"].replace({"CNG":"","Electric":"","LPG":""}, regex=True)
nan_value = float("NaN")
car_data["fuel_type"] = car_data["fuel_type"].replace("",nan_value)
car_data.dropna(inplace=True)
print(car_data["fuel_type"].unique())

#print(car_data["transmission_type"].unique())
car_data["transmission_type"]= car_data["transmission_type"].astype("category")


#print(car_data["mileage"].unique())
car_data["mileage"] = car_data["mileage"].replace({"Mileage":"", " kmpl":"",\
                                "km/kg":"", "km/hr":"", " ":""}, regex = True)
car_data["mileage"] = car_data["mileage"].astype("float64")


#print(car_data["max_power"].unique())
car_data["max_power"] = car_data["max_power"].replace({"Max":""," ":"",\
                                            "bhp":"", "Power":"","Seats5":"", "SeatsN/A":"","Seats8":""}, regex = True)
#print(car_data["max_power"].unique())
nan_value = float("NaN")
car_data["max_power"] = car_data["max_power"].replace("",nan_value)
car_data.dropna(inplace=True)
car_data["max_power"] = car_data["max_power"].astype("float64")

car_data.drop_duplicates(keep='first',inplace=True)

car_data["year"] = car_data["year"].astype("int64")
#print(car_data.info())


# IQR for Selling Price
Q1 = car_data["selling_price"].quantile(0.25)
Q3 = car_data["selling_price"].quantile(0.75)

IQR = Q3 - Q1
 
lower = Q1 - 20*IQR
upper = Q3 + 20*IQR

''' Removing the Outliers '''
car_data = car_data[(car_data["selling_price"]>lower)&\
                    (car_data["selling_price"]<upper)]

    
    
# IQR for Selling Price
Q1 = car_data["mileage"].quantile(0.25)
Q3 = car_data["mileage"].quantile(0.75)

IQR = Q3 - Q1
 
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

''' Removing the Outliers '''
car_data = car_data[(car_data["mileage"]>lower)&\
                    (car_data["mileage"]<upper)]
    
    
    
pd.set_option('display.max_rows', None)
print(car_data.info())
#print(car_data.head(10))
#print(car_data.describe())

print(car_data["fuel_type"].unique())
# export the data set after cleaning
car_data.to_csv("car_cleaned.csv", index = False)

#print(car_data.corr())

sns.set(style="darkgrid")
sns.regplot(x=car_data["seller_type"],y=car_data["selling_price"], marker="*",fit_reg = False)