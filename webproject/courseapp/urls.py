from django.urls import path
from . import views

urlpatterns = [
    path("error/", views.err, name='error'),
    path("", views.home, name='courseapp'),

    path("addnew/", views.addnew, name='addnewC'),
    path("save/", views.savedata, name='savedataC'),

    path("edit/<int:id>/", views.edit, name='editC'),
    path("update/<int:id>", views.update, name='updateC'),

    path("del/<int:id>/", views.dlt, name='dltC'),
]