from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('Tlogin/',views.tlog),
    path('Tregister/',views.treg),
    path('Thome/',views.thome),
    path('Tlogout/',views.tlogout),
    path('TMaterials/',views.eventmaterials),
    path('Tinteriormaterials/',views.interiormaterials),
]