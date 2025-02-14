from django.shortcuts import render
from .models import Question, Answer, UserResponse

# Create your views here.

def questionnaire_view(request):
	questions = Question.objects.prefetch_related('answer_set').all()
	success_message = None

	if request.method == 'POST':
		for question in questions:
			question_key = f'question_{question.id}'

			if question.question_type in ['single', 'multiple']:
				user_answer = request.POST.getlist(question_key)
				for answer_id in user_answer:
					answer = Answer.objects.get(id=answer_id)
					UserResponse.objects.update_or_create(
						user=request.user,
						question=question,
						defaults={'answer': answer},
					)
			elif question.question_type == 'text':
				text_response = request.POST.get(question_key)
				if text_response:
					UserResponse.objects.update_or_create(
						user=request.user,
						question=question,
						defaults={'text_response': text_response},
					)

		success_message = "Thank you! Your responses have been saved."

	return render(request, 'questionnaire/questionnaire.html', {
		'questions': questions,
		'success_message': success_message,
	})
