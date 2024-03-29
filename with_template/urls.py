from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('params/<str:name>', views.show),
    path('list', views.list),
    path('fizzbuzz/<int:limit>', views.fizzbuzz,name="fizzbuzz"),
    path('form', views.form, name="form"),
    path('form_read', views.form_read, name='form_read'),
]