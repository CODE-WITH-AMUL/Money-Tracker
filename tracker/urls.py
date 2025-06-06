from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('dashbord/', views.dashboard, name='dashboard'),
    path('' , index , name='index'),
] 