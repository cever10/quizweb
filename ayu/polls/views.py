from django.shortcuts import render
from django.http import HttpResponse
from .models import RandomQuiz
from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz
from .forms import QuizForm




def index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'polls/index.html', {'quizzes': quizzes})

def random_quiz(request):
    random_quiz = RandomQuiz.objects.order_by('?').first() 
    context = {'random_quiz': random_quiz}
    return render(request, 'polls/random_quiz.html', context)

def check_answer(request):
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz_id')
        user_answer = request.POST.get('user_answer')

        # 퀴즈 ID를 이용하여 퀴즈 객체를 가져옵니다.
        random_quiz = RandomQuiz.objects.get(pk=quiz_id)

        # 사용자의 답변과 정답을 비교합니다.
        if user_answer == random_quiz.answer:
            answer_result = "정답입니다!"
        else:
            answer_result = f"틀렸습니다. 정답은 {random_quiz.answer}입니다."

        return render(request, 'polls/random_quiz.html', {'random_quiz': random_quiz, 'answer_result': answer_result})
    
def random_quiz_view(request):
    random_quiz = RandomQuiz.objects.order_by('?').first()  # 랜덤 퀴즈 선택
    context = {'random_quiz': random_quiz}
    return render(request, 'polls/random_quiz.html', context)

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'polls/quiz_list.html', {'quizzes': quizzes})

def quiz_create(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # index 페이지로 이동
    else:
        form = QuizForm()
    return render(request, 'polls/quiz_form.html', {'form': form})

def quiz_update(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('index')  # index 페이지로 이동
    else:
        form = QuizForm(instance=quiz)
    return render(request, 'polls/quiz_form.html', {'form': form})

def quiz_delete(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        quiz.delete()
        return redirect('index')  # index 페이지로 이동
    return render(request, 'polls/quiz_confirm_delete.html', {'quiz': quiz})

def subjective_quiz(request):
    return HttpResponse("주관식 퀴즈 페이지")

def timed_quiz(request):
    return HttpResponse("제한 시간 페이지")
