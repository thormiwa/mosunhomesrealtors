from django.urls import path
from . import views

app_name = "blog"   


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('contact/', views.contact, name="contact"),
]