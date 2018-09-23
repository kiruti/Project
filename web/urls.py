from django.contrib import admin
from django.urls import path

from web import views

urlpatterns = [

    path('', views.index),
    path('buidlings/<int:building_id>/rooms', views.rooms_edit),
    path('api/buildings/<int:building_id>/indoor', views.buildling_api_indoor, name="buildling_api_indoor"),
    path('rooms', views.rooms_create, name="rooms_create"),
]
