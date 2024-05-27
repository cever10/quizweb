"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.mainPage, name='mainPage'),

    path('uRegisterPage', views.uRegisterPage, name='uRegisterPage'),
    path('uLoginPage', views.uLoginPage, name='uLoginPage'),
    path('uLogout', views.uLogout, name='uLogout'),

    path('createRPage/', views.createRPage, name='createRPage'),
    path('createSPage/', views.createSPage, name='createSPage'),
    path('createTPage/', views.createTPage, name='createTPage'),

    path('listRPage/', views.listRPage, name='listRPage'),
    path('listPage/', views.listSPage, name='listSPage'),
    path('listTPage/', views.listTPage, name='listTPage'),

    path('modifyRPage/', views.modifyRPage, name='modifyRPage'),
    path('modifyPage/', views.modifySPage, name='modifySPage'),
    path('modifyTPage/<int:quizID>', views.modifyTPage, name='modifyTPage'),

    path('delRPage/', views.delRPage, name='delRPage'),
    path('delPage/', views.delSPage, name='delSPage'),
    path('delTPage/<int:quizID>', views.delTPage, name='delTPage'),

    path('randomPage/', views.randomPage, name='randomPage'),
    path('subjectivePage/', views.subjectivePage, name='subjectivePage'),
    path('TLPage/', views.TLPage, name='TLPage'),

    path('checkAnswer/', views.checkAnswer, name='checkAnswer'),

    #--------------------------------------------------------------------
    path('', views.index, name='index'),
    path('random_quiz/', views.random_quiz, name='random_quiz'),
    path('random_quiz/get_next_random_quiz/', views.get_next_random_quiz, name='get_next_random_quiz'),
    path('check_answer/', views.check_answer, name='check_answer'),
    path('subjective_quiz/', views.subjective_quiz, name='subjective_quiz'),
    path('timed_quiz/', views.timed_quiz, name='timed_quiz'),
    path('quiz/', views.quiz_list, name='quiz_list'),
    path('quiz/create/', views.quiz_create, name='quiz_create'),
    path('quiz/list/', views.listRPage, name='listRPage'),
    path('quiz/<int:pk>/update/', views.quiz_update, name='quiz_update'),
    path('quiz/<int:pk>/delete/', views.quiz_delete, name='quiz_delete'),
]
