from django.urls import path
from .import views
urlpatterns=[
    path('',views.home),
    path('Slogin/',views.log2),
    path('Sregister/',views.reg2),
    path('Shome/',views.Shome),
    path('Slogout/',views.Slogout),
    path('clientlogindetails/',views.client_details),
    path('LApproval/<int:id>/',views.loginapproval),
    path('clientregdetails/',views.client_regdetails),
    path('CDapproval/<int:id>/',views.cdapproval),
    path('Interiordetails/',views.client_interiordetails),
    path('Interiorapproval/<int:id>/',views.interiorapproval),
    path('Edetails/',views.Ematerialdetails),
    path('Eapproval/<int:id>/',views.Ematerialsapproval),
    path('InteriorMaterial/',views.Imaterialdetails),
    path('Iapproval/<int:id>/',views.Imaterialsapproval),

]