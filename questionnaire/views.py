from django.shortcuts import render
from .models import Question

# Create your views here.

def questionnaire_view(request):
	questions = Question.objects.all()
	return render(request, 'questionnaire/questionnaire.html', {'questions': questions})
