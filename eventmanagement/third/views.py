from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def home(request):
    return render(request,"home.html")


def treg(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        phonenumber = request.POST["phonenumber"]
        gender = request.POST["gender"]

        try:
            tevents(name=name, email=email, password=password, phonenumber=phonenumber, gender=gender).save()
            messages.info(request, 'Your Register successfully!')
            return redirect('/Tlogin/')
        except:
            return ('/')
            print("done")
    return render(request, 'third/tregister.html')


def tlog(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            emp = tevents.objects.get(email=email, password=password)
            messages.success(request, 'You Have Logged In')
            request.session['P'] = emp.email
            return render(request, 'third/thome.html')

        except:
            messages.success(request, 'Unauthorized UserName and Password')
            return redirect('/Tlogin/')

    return render(request, 'third/tlogin.html')

def thome(request):
    return render(request,"third/thome.html")

def tlogout(request):
    if 'user' in request.session:
        request.session.pop('user',None)
        messages.success(request,'Logout Successfully')
        return redirect('/')
    else:
        messages.success(request, 'Session Logged Out')
        return render(request,'home.html')


def eventmaterials(request):
    if request.method == "POST":
        name = request.POST["name"]
        table = request.POST["table"]
        quantity = request.POST["quantity"]
        projector = request.POST["projector"]
        quantity1 = request.POST["quantity1"]
        mike = request.POST["mike"]
        quantity2 = request.POST["quantity2"]
        Tv = request.POST["Tv"]
        quantity3 = request.POST["quantity3"]
        conditions = request.POST["conditions"]
        quantity4 = request.POST["quantity4"]
        led = request.POST["led"]
        quantity5 = request.POST["quantity5"]
        value = request.POST["value"]

        events(name=name, table=table, quantity=quantity, projector=projector, quantity1=quantity1, mike=mike, quantity2=quantity2, Tv=Tv, quantity3=quantity3, conditions=conditions,quantity4=quantity4,led=led,quantity5=quantity5,value=value).save()
        messages.info(request,"Details Submitted")
        return redirect('/Thome/')

    return render(request,"third/Material Details.html")

def interiormaterials(request):
    if request.method == "POST":
        name = request.POST["name"]
        boards = request.POST["boards"]
        woods = request.POST["woods"]
        Tables = request.POST["Tables"]
        Designs = request.POST["Designs"]
        wallpapers = request.POST["wallpapers"]
        others = request.POST["others"]
        quantity = request.POST["quantity"]
        quantity1 = request.POST["quantity1"]
        quantity2 = request.POST["quantity2"]
        quantity3 = request.POST["quantity3"]
        quantity4 = request.POST["quantity4"]
        quantity5 = request.POST["quantity5"]
        value = request.POST["value"]

        interior(name=name, boards=boards, woods=woods, Tables=Tables, Designs=Designs, wallpapers=wallpapers,others=others, quantity=quantity, quantity1=quantity1, quantity2=quantity2,quantity3=quantity3,quantity4=quantity4,quantity5=quantity5, value=value).save()
        messages.info(request,"Your Details Submitted Successfully!")
        return redirect('/Thome/')
    return render(request,"third/Interior materials.html")

