from django.urls import path
from . import views

app_name = 'watcher'

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('watch/', views.Watch.as_view(), name="watch"),
    path('hero/<int:pk>/detail/', views.HeroDetailView.as_view(), name="hero_detail"),
    path('hero/<int:pk>/edit/', views.HeroUpdateView.as_view(), name="hero_update"),
    path('heor/create/', views.HeroCreateView.as_view(), name="hero_create"),
]
