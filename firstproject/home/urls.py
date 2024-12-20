from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('about/', views.about),
    path('dynamic_route/<int:number>', views.dynamic_route),
    path('thank-you/', views.thank_you),
    path('search_page/', views.search_page),
]   
