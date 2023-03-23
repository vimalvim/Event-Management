from django.shortcuts import render,redirect
from django.contrib import messages
from second.models import *
from first.models import *
from third.models import *



def home(request):
    return render(request,"home.html")

def reg2(request):
    if request.method == "POST":
            name = request.POST["name"]
            email = request.POST["email"]
            password = request.POST["password"]
            phonenumber = request.POST["phonenumber"]
            gender = request.POST["gender"]

            try:
                event(name=name, email=email, password=password, phonenumber=phonenumber, gender=gender).save()
                messages.info(request, 'Your Register successfully!')
                return redirect('/Slogin/')
            except:
                return ('/')
                print("done")
    return render(request, 'second/sregister.html')

def log2(request):
    if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            try:
                emp = event.objects.get(email=email, password=password)
                messages.success(request, 'You Have Logged In')
                request.session['P'] = emp.email
                return render(request, 'second/Shome.html')

            except:
                messages.success(request, 'Unauthorized UserName and Password')
                return redirect('/Slogin/')

    return render(request, 'second/slogin.html')

def Shome(request):
    return render(request,"second/Shome.html")

def Slogout(request):
    if 'user' in request.session:
        request.session.pop('user',None)
        messages.success(request,'Logout Successfully')
        return redirect('/')
    else:
        messages.success(request, 'Session Logged Out')
        return render(request,'home.html')


def client_details(request):
        da = register1.objects.all()
        return render(request,"second/clientapproval.html", {'da':da})

def loginapproval(request, id):
        datas = register1.objects.get(id=id)
        datas.report = True
        datas.save()
        print('hi')
        messages.info(request, "Client has been Allowed to Log-In")
        return redirect('/Shome/')


def client_regdetails(request):
        da = detail.objects.filter(report=False)
        return render(request, "second/cd approval.html", {'da': da})


def cdapproval(request, id):
        data = detail.objects.get(id=id)
        data.report = True
        data.save()
        messages.info(request, "Management has been Approved ")
        return redirect('/clientregdetails/')


def client_interiordetails(request):
    da=designing.objects.filter(report=False)
    return render(request, "second/interior approval.html", {'da':da})


def interiorapproval(request,id):
    data = designing.objects.get(id=id)
    data.report = True
    data.save()
    messages.info(request, "Your details has been approved by Management")
    return redirect('/Interiordetails/')

def Ematerialdetails(request):
    da = events.objects.filter(report=False)
    return render(request, "second/Event materials approval.html", {'da': da})

def Ematerialsapproval(request, id):
    data = events.objects.get(id=id)
    data.report = True
    data.save()
    messages.info(request, "Your details has been approved by Management")
    return redirect('/Edetails/')


def Imaterialdetails(request):
    da = interior.objects.filter(report=False)
    return render(request, "second/Interior materials approval.html", {'da': da})

def Imaterialsapproval(request, id):
    data = interior.objects.get(id=id)
    data.report = True
    data.save()
    messages.info(request, "Your details has been approved by Management")
    return redirect('/InteriorMaterial/')





