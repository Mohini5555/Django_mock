from django.urls import path
from app1 import views

APP_NAME ="app1"

urlpatterns = [
    path('', views.index, name="index_map1"),
    path('render_method/', views.render_method, name="render_method"),
]

