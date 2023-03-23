from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('flogin/',views.flog),
    path('fregister/',views.freg),
    path('fhome/',views.fhome),
    path('flogout/',views.flogout),
    path('fcompany/',views.company),
    path('Interiorcompany/',views.Icompany),
    path('EventPrediction/',views.Epredict),
    path('InteriorPrediction/',views.Ipredict),
    path('predictalgo/', views.predictalgo),
    path('Eprediction/<int:id>/', views.prediction),
    path('Ipredictalgo/', views.Interiorpredictalgo),
    path('Iprediction/<int:id>/', views.Interiorprediction),
]