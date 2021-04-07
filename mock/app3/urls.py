from django.urls import path
from app3 import views

APP_NAME ="app3"

urlpatterns = [
    path('index3/', views.index, name="index_map3"),
    path('add/<num1>/<num2>', views.add, name="add"),
    path('display/<data>', views.display, name="display"),
]

