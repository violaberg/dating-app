from django.shortcuts import render
from .models import Question, Answer, UserResponse
from profiles.models import Profile

# Create your views here.

def questionnaire_view(request):
	questions = Question.objects.prefetch_related('answer_set').all()
	success_message = None
	profile = Profile.objects.get(user=request.user)

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

		question_to_field_mapping = {
			1: 'age_preference',
			2: 'gender_preference',
			3: 'spark_type',
		}

		for question_id, field_name in question_to_field_mapping.items():
			user_responses = UserResponse.objects.filter(
				user=request.user,
				question_id=question_id,
			)
			for user_response in user_responses:
				if user_response.question.question_type == 'single' and user_response.answer:
					answer_value = user_response.answer.answer_text
					setattr(profile, field_name, answer_value)
				elif user_response.question.question_type == 'multiple' and user_response.answer:
					answer_value_list = []
					if user_response.answer:
						answer_value_list.append(user_response.answer.answer_text)
					answer_value = ', '.join(answer_value_list)
					setattr(profile, field_name, answer_value)
	profile.save()

	success_message = "Thank you! Your responses have been saved."

	return render(request, 'questionnaire/questionnaire.html', {
		'questions': questions,
		'success_message': success_message,
	})
