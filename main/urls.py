from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Пустой путь ведет на главную страницу
    path('home', views.index, name='home'),  # Дублирующий маршрут для "home"
    path('about/', views.about, name='about')  # Маршрут для "About"
]
