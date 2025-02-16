from django import forms
from crispy_forms.helper import FormHelper
from .models import UserResponse, Question, Choice

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['spark_type', 'gender_preferences', 'age_preferences']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get questions by type
        spark_q = Question.objects.get(question_type='SINGLE', order=1)
        gender_q = Question.objects.get(question_type='MULTIPLE', order=2)
        age_q = Question.objects.get(question_type='MULTIPLE', order=3)

        # Set up form fields
        self.fields['spark_type'] = forms.ModelChoiceField(
            queryset=Choice.objects.filter(question=spark_q),
            widget=forms.RadioSelect,
            label=spark_q.question_text,
            required=True
        )

        self.fields['gender_preferences'] = forms.ModelMultipleChoiceField(
            queryset=Choice.objects.filter(question=gender_q),
            widget=forms.CheckboxSelectMultiple,
            label=gender_q.question_text,
            required=True
        )

        self.fields['age_preferences'] = forms.ModelMultipleChoiceField(
            queryset=Choice.objects.filter(question=age_q),
            widget=forms.CheckboxSelectMultiple,
            label=age_q.question_text,
            required=True
        )

        # Crispy Forms setup
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = 'mb-2'
        self.helper.field_class = 'mb-4'
