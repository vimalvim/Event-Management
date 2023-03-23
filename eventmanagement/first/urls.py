from django.urls import path
from .import views
urlpatterns=[
    path('',views.home),
    path('Register/',views.register),
    path('Login/',views.login),
    path('home1/',views.home1),
    path('Logout/',views.logout),
    path('Cdetails/',views.client_event),
    path('Cinteriordetails/',views.client_interior),
]