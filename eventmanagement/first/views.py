from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *



def home(request):
    return render(request,"home.html")

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        phonenumber = request.POST["phonenumber"]
        gender = request.POST["gender"]

        try:
            register1(name=name, email=email, password=password, phonenumber=phonenumber, gender=gender).save()
            messages.info(request, 'Your Register successfully!')
            return redirect('/Login/')
        except:
            return ('/')
            print("done")
    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        email =request.POST["email"]
        password = request.POST["password"]

        try:
            emp = register1.objects.get(email=email, password=password)
            if emp.report == True:
                request.session['user'] = email
                messages.info(request, 'Your login successfully! and session started')
                return redirect('/home1/')
            else:
                messages.info(request, 'Your can not login! Need Management approval!!!')

        except:
            pass

    return render(request, 'login.html')


def home1(request):
    return render(request,"home1.html")


def logout(request):
    if 'user' in request.session:
        request.session.pop('user', None)
        messages.success(request, 'Logout Successfully')
        return redirect('/')
    else:
        messages.success(request, 'Session Logged Out')
        return render(request, 'home.html')


def client_event(request):
    if request.method == "POST":
        firstname=request.POST["firstname"]
        email=request.POST["email"]
        phonenumber=request.POST["phonenumber"]
        address=request.POST["address"]
        city=request.POST["city"]
        country=request.POST["country"]
        Events = request.POST["Events"]
        food=request.POST["food"]
        attendees=request.POST["attendees"]
        date=request.POST["date"]
        Time=request.POST["Time"]
        message=request.POST["message"]
        drinks = request.POST["drinks"]
        beverages = request.POST["beverages"]
        service = request.POST["service"]
        Decoration = request.POST["Decoration"]
        Specialized= request.POST["Specialized"]
        Budget = request.POST["Budget"]

        try:
            detail(firstname=firstname, email=email, phonenumber=phonenumber, address=address, city=city, country=country, Events=Events, food=food, attendees=attendees, date=date, Time=Time,message=message, drinks=drinks, beverages=beverages,service=service,Decoration=Decoration, Budget=Budget,Specialized=Specialized).save()
            messages.info(request,"your details have been submitted successfully")
            return redirect("/home1/")
        except:
            return('/')
            print("done")
    return render(request,"clientdetails.html")

def client_interior(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        address = request.POST["address"]
        city = request.POST["city"]
        country = request.POST["country"]
        area = request.POST["area"]
        structure = request.POST["structure"]
        ventilation = request.POST["ventilation"]
        windows = request.POST["windows"]
        walls = request.POST["walls"]
        floor = request.POST["floor"]
        budget = request.POST["budget"]
        message = request.POST["message"]
        feet = request.POST["feet"]

        designing(firstname=firstname, email=email, phonenumber=phonenumber, address=address, city=city, country=country, area=area, budget=budget, message=message, feet=feet, walls=walls, floor=floor, structure=structure, ventilation=ventilation, windows=windows).save()
        messages.info(request, "your details have been submitted successfully")
        return redirect("/home1/")
    return render(request,"client interior.html")


