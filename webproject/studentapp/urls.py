from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homeS'),

    path('addnew/', views.addnew, name='addnewS'),
    path('save/', views.savedata, name='savedataS'),



    path('edit/<int:id>/', views.edit, name='editS'),
    path('update/<int:id>/', views.update, name='updateS'), 

    path('delete/<int:id>/', views.rem, name='deleteS'), 




]