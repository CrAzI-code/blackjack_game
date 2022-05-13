from django.urls import path
from . import views

app_name = "birth_certificate"
urlpatterns = [
    path('', views.index, name= "index"),
    path('about/', views.about, name="about"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),    
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout")
    ]