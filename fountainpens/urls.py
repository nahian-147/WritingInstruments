from django.urls import path
from . import views

urlpatterns = [
    path('', views.showAllFountainPens,name='showAllFountainPens'),
    path('add-fountain-pen/', views.addNewFountainPen,name='addNewFountainPen'),
    path('nibs/', views.showAllNibs,name='showAllNibs'),
    path('add-new-nib/', views.addNewNib,name='addNewNib'),
]