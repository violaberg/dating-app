from django.urls import path
from . import views

urlpatterns = [
	path('', views.questionnaire_view, name='questionnaire'),
]
