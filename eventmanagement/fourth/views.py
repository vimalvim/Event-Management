from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from first.models import *
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier

import warnings

warnings.filterwarnings('ignore')
from sklearn.linear_model import Perceptron


def home(request):
    return render(request,"home.html")

def freg(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        phonenumber = request.POST["phonenumber"]
        gender = request.POST["gender"]

        try:
            fevents(name=name, email=email, password=password, phonenumber=phonenumber, gender=gender).save()
            messages.info(request, 'Your Register successfully!')
            return redirect('/flogin/')
        except:
            print("done")
            return ('/')

    return render(request, 'fourth/fregister.html')

def flog(request):
    if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            try:
                emp =fevents .objects.get(email=email, password=password)
                messages.success(request, 'You Have Logged In')
                request.session['P'] = emp.email
                return render(request, 'fourth/fhome.html')

            except:
                messages.success(request, 'Unauthorized UserName and Password')
                return redirect('/flogin/')
    return render(request, 'fourth/flogin.html')

def fhome(request):
    return render(request,"fourth/fhome.html")

def flogout(request):
    if 'user' in request.session:
        request.session.pop('user',None)
        messages.success(request,'Logout Successfully')
        return redirect('/')
    else:
        messages.success(request, 'Session Logged Out')
        return render(request,'home.html')

def company(request):
    if request.method == "POST":
        name = request.POST["name"]
        address = request.POST["address"]
        services = request.POST["services"]
        specialized = request.POST["specialized"]
        experience = request.POST["experience"]
        employees = request.POST["employees"]
        budget = request.POST["budget"]
        number = request.POST["number"]

        eventcompany(name=name, address=address, budget=budget, number=number, services=services,specialized=specialized,experience=experience,employees=employees).save()
        messages.info(request,"Company Details Submitted Successfully!")
        return redirect('/fhome/')
    return render(request,"fourth/company details.html")

def Icompany(request):
    if request.method == "POST":
        name = request.POST["name"]
        address = request.POST["address"]
        services = request.POST["services"]
        specialized = request.POST["specialized"]
        experience = request.POST["experience"]
        employees = request.POST["employees"]
        budget = request.POST["budget"]
        number = request.POST["number"]

        Interiorcompany(name=name, address=address, budget=budget, number=number, services=services,specialized=specialized,experience=experience,employees=employees).save()
        messages.info(request, "Company Details Submitted Successfully!")
        return redirect('/fhome/')
    return render(request,"fourth/Interior company.html")

def Epredict(request):
    da = detail.objects.all()
    return render(request,"fourth/Epredict.html",{'da':da})

def Ipredict(request):
    da = designing.objects.all()
    return render(request,"fourth/Ipredict.html",{'da':da})


def predictalgo(datas,r):
    data = pd.read_csv("a.csv")

    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = GradientBoostingClassifier()
    model.fit(data_x, data_y)
    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)

    return predicted[0]


def prediction(request,id):
    data=detail.objects.get(id=id)
    r=data.id
    aa1=data.Events
    aa2=data.Specialized
    aa3=data.Budget
    print("events",aa1)
    print("specialized", aa2)
    print("Budget",aa3)
    xx=predictalgo([aa1,aa2,aa3],r)
    start=detail.objects.filter(id=r).update(Output=xx)
    print(start)
    messages.info(request,"Predicted Sucessfully ")
    return redirect('/EventPrediction/')

def Interiorpredictalgo(datas,r):
    data = pd.read_csv("Interior.csv")
    xx = data.drop('Specialized', axis=1, inplace=True)
    print(data.head())
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = GradientBoostingClassifier()
    model.fit(data_x, data_y)
    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)

    return predicted[0]


def Interiorprediction(request,id):
    data=designing.objects.get(id=id)
    r=data.id
    aa1=data.area
    aa2=data.budget
    print("area",aa1)
    print("budget",aa2)
    xx=Interiorpredictalgo([aa1,aa2],r)
    start=designing.objects.filter(id=r).update(Output=xx)
    print(start)
    messages.info(request,"Predicted Sucessfully ")
    return redirect('/InteriorPrediction/')






