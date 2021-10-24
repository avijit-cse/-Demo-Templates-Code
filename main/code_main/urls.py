from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeView, name="home"),
    path('about/', views.about, name="about"),
    path('con/', views.contract, name="contract"),
    path('login/', views.Login, name="login"),
    path('ragistration/', views.Ragistarion, name="ragistion"),
    path('sss/', views.Sview, name="seri"),
]
