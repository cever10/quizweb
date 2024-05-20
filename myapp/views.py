from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from myapp import forms, models


from .models import RandomQuiz
from .models import Quiz
from .forms import QuizForm
from .models import SubjectiveQuiz
from .forms import SubjectiveQuizForm
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.

def mainPage(request):
    return render(request, 'main.html')



def uRegisterPage(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainPage')
    else:
        form = forms.UserForm()
        return render(request, 'uRegister.html', {'form': form})


def uLoginPage(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pw = request.POST.get('password')

        users = User.objects.filter(username=name)
        if users.exists():
            user = users.first()
            if name == user.username and pw == user.password:
                login(request, user)
                return redirect('mainPage')
            else:
                return render(request, 'uLogin.html')
        else:
            return render(request, 'uLogin.html')
    else:
        return render(request, 'uLogin.html')
    

def uLogout(request):
    logout(request)
    return redirect('mainPage')



def createRPage(request):
    return render(request, 'createR.html')


def createSPage(request):
    return render(request, 'createS.html')


def createTPage(request):
    if request.method == 'POST':
        form = forms.TLQuizForm(request.POST)
        if form.is_valid():
            userID = request.user.id
            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']

            formFixed = models.TLQuiz(userID=userID, question=question, answer=answer)
            formFixed.save()

            return redirect('mainPage')
    else:
        form = forms.TLQuizForm()
        return render(request, 'createT.html', {'form': form})
    


def listRPage(request):
    return render(request, 'listR.html')


def listSPage(request):
    return render(request, 'listS.html')


def listTPage(request):
    #TLQuiz = models.TLQuiz.objects.all()
    currentUserID = request.user.id
    TLQuiz = models.TLQuiz.objects.filter(userID=currentUserID)
    return render(request, 'listT.html', {'TLQuiz': TLQuiz})



def modifyRPage(request):
    return render(request, 'modifyR.html')


def modifySPage(request):
    return render(request, 'modifyS.html')


def modifyTPage(request, quizID):
    quiz = models.TLQuiz.objects.get(pk=quizID)

    if request.method == 'POST':
        form = forms.TLQuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('listTPage')
    else:
        form = forms.TLQuizForm(instance=quiz)

    return render(request, 'modifyT.html', {'form': form, 'quizID': quizID})



def delRPage(request):
    return render(request, 'delR.html')


def delSPage(request):
    return render(request, 'delS.html')


def delTPage(request, quizID):
    quiz = models.TLQuiz.objects.get(pk=quizID)
    quiz.delete()

    return redirect('listTPage')



def randomPage(request):
    return render(request, 'random.html')


def subjectivePage(request):
    return render(request, 'subjective.html')


def TLPage(request):
    TLQuiz = models.TLQuiz.objects.order_by('?').first()
    
    if request.user.is_authenticated == True:
        request.session[f'quizStartTime{request.user.id}'] = timezone.now().isoformat()

    return render(request, 'TL.html', {'TLQuiz': TLQuiz, 'end': False})



def checkAnswer(request):
    if request.method == 'POST':
        quizID = request.POST.get('quizID')
        userAnswer = request.POST.get('userAnswer')

        
        # 퀴즈 ID를 이용하여 퀴즈 객체를 가져옵니다.
        TLQuiz = models.TLQuiz.objects.get(pk=quizID)


        startTimeStr = request.session.get(f'quizStartTime{request.user.id}')
        if startTimeStr:
            startTime = timezone.datetime.fromisoformat(startTimeStr)
            currentTime = timezone.now()
            checkedTime = (currentTime - startTime).total_seconds()

        if checkedTime <= float(TLQuiz.timeLimit) + 0.1:
            # 사용자의 답변과 정답을 비교합니다.
            if userAnswer == TLQuiz.answer:
                answerResult = "정답입니다!"
            else:
                answerResult = f"틀렸습니다. 정답은 {TLQuiz.answer}입니다."
        else:
            answerResult = "비정상 제출 시간입니다"

    return render(request, 'TL.html', {'TLQuiz': TLQuiz, 'answerResult': answerResult, 'end': True})



#-----------------------------------------------------------------------------

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
    
def get_next_random_quiz(request):
    random_quiz = RandomQuiz.objects.order_by('?').first()
    
    # 선택된 퀴즈의 정보를 JSON 형식으로 반환
    data = {
        
        'id': random_quiz.id,
        'title': random_quiz.title,
        'content': random_quiz.content,
    }
    
    return JsonResponse(data)

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


#def subjective_quiz(request):
#    return HttpResponse("주관식 퀴즈 페이지")

def timed_quiz(request):
    return HttpResponse("제한 시간 페이지")


def subjective_quiz(request) :
    if request.method == 'POST':
        form = SubjectiveQuizForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('subjective_quiz')
    else :
        form = SubjectiveQuizForm()

    quizzes = SubjectiveQuiz.objects.all()
    return render(request, 'polls/subjective_quiz.html', {'form' : form, 'quizzes' : quizzes})
