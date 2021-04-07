from django.urls import path
from app2 import views

APP_NAME ="app2"

urlpatterns = [
    path('index2/', views.index, name="index_map2"),
    path('render_method2/', views.render_method, name="render_method2"),
]

