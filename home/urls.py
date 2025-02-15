from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('faq/', views.faq, name='faq'),
]
