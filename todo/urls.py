from django.urls import path
from todo import views
from todo import models
from todo import forms
urlpatterns=[
    path("",views.create,name='create'),
    path("read/",views.read,name='read'),
    path("update/<int:id>",views.update,name='update'),
    path("delete/<int:id>",views.delete,name='delete'),
]