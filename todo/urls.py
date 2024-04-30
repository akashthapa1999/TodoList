from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.home, name = "showdata"),
    path("delete/<int:id>", views.delete, name = "deletedata"),
    path("update/<int:id>", views.update, name = "updatedata"),

]
