from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='event'),
    path('registration/', views.reg, name='reg'),
]