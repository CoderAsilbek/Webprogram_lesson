from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),#it is for nothing after hello
    path("<str:name>", views.greet, name="anyName"),
    path("asilbek", views.asilbek, name="Asilbek")

]