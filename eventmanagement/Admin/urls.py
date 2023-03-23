from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('Adminlogin/',views.Alog),
    path('Adminhome/', views.Ahome),
    path('Alogout/',views.Alogout),
    path('viewclientdetails/',views.clientdetails),
    path('viewInteriordetails/',views.interiordetails),
    path('viewEventmaterials/',views.Eventmaterilas),
    path('viewInteriormaterials/',views.Interiormaterials),
    path('Eventcompanydetails/',views.Eventcompany),
    path('Interiorcompanydetails/',views.Interiorcompany1),
]