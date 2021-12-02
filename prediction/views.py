from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np

# Create your views here.

import joblib

model = joblib.load('./models/car_model.joblib')
car=pd.read_csv('car_cleaned.csv')


def carpage(request):
    companies = sorted(car['company'].unique())
    car_models = sorted(car['full_name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')
    return render(request, 'prediction/carpage.html', {"companies":companies, "car_models":car_models,\
         "years":year, "fuel_types":fuel_type})


def predict(request):
    if request.method == 'POST':
        temp ={}
        #temp["company"]=request.POST.get('company')
        #temp["car_model"]=request.POST.get('car_models')
        temp['year'] =request.POST.get('year')
        temp["Fuel_Type_Petrol"]=request.POST.get('fuel_type')
        if(temp["Fuel_Type_Petrol"]=='Petrol'):
                temp["Fuel_Type_Petrol"]=1
                temp["Fuel_Type_Petrol"]=0
        else:
            temp["Fuel_Type_Petrol"]=0
            temp["Fuel_Type_Petrol"]=1
        temp['driven']=request.POST.get('kilo_driven')
        temp['mileage']=request.POST.get('mileage')
        temp['max_power']=request.POST.get('max_power')
        testDtaa=pd.DataFrame({'x':temp}).transpose()
        prediction=model.predict(testDtaa)[0]
        prediction= round(np.exp(prediction),2)
        context={'prediction':prediction,'temp':temp}

    return render(request,'prediction/carpage.html',context)