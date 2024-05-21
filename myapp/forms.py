from django.contrib.auth.models import User # type: ignore

from django import forms # type: ignore
from myapp import models

from .models import RandomQuiz
from .models import Quiz
from .models import SubjectiveQuiz


class TLQuizForm(forms.ModelForm):
    class Meta:
        model = models.TLQuiz
        fields = ['question', 'answer', 'timeLimit']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


#--------------------------------------------------

class RandomQuizForm(forms.ModelForm):
    # 사용자가 답변을 입력할 수 있는 필드를 추가함.
    answer_field = forms.CharField( max_length=100)

class RandomQuizForm(forms.ModelForm):
    class Meta:
        model = RandomQuiz
        fields = ['title', 'content', 'answer']
        
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['question', 'answer']

class SubjectiveQuizForm(forms.ModelForm) :
    class Meta :
        model = SubjectiveQuiz
        fields = ['question', 'answer']