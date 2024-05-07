# polls/forms.py

from django import forms
from .models import RandomQuiz
from .models import Quiz

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