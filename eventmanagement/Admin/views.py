from django.shortcuts import render, redirect
from django.contrib import messages
from first.models import *
from third.models import *
from fourth.models import *

def home(request):
    return render(request,"home.html")


def Alog(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == "admin@gmail.com" and password == "admin":
            request.session['admin'] = 'admin@gmail.com'
            messages.info(request, "Successfully Login")
            return redirect('/Adminhome/')
        elif email != "admin@gmail.com":
            messages.error(request, "Wrong Admin Email")
            return redirect('/Adminlogin/')
        elif password != "admin":
            messages.error(request, "Wrong Admin Password")
            return redirect('/Adminlogin/')
    return render(request, 'admin/alogin.html')


def Ahome(request):
    return render(request,"admin/ahome.html")

def Alogout(request):
        if 'admin' in request.session:
            request.session.pop('admin', None)
            messages.success(request, 'Logout Successfully')
            return redirect('/')
        else:
            messages.success(request, 'Session Logged Out')
        return render(request, 'home.html')

def clientdetails(request):
    da = detail.objects.filter(report=True)
    return render(request,"admin/clientdetails.html", {'da':da})

def interiordetails(request):
    da = designing.objects.filter(report=True)
    return render(request,"admin/ainterior.html", {'da':da})

def Eventmaterilas(request):
    da = events.objects.filter(report=True)
    return render(request,"admin/Event materials.html", {'da':da})

def Interiormaterials(request):
    da = interior.objects.filter(report=True)
    return render(request,"admin/Interior materials.html", {'da':da})

def Eventcompany(request):
    da = eventcompany.objects.all()
    return render(request,"admin/Ecompany.html",{'da':da})

def Interiorcompany1(request):
    da = Interiorcompany.objects.all()
    return render(request,"admin/Icompany.html",{'da':da})