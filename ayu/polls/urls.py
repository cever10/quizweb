from django.urls import path
from . import views 

urlpatterns = [

    path('', views.index, name='index'),
    path('random_quiz/', views.random_quiz, name='random_quiz'),
    path('check_answer/', views.check_answer, name='check_answer'),
    path('subjective_quiz/', views.subjective_quiz, name='subjective_quiz'),
    path('timed_quiz/', views.timed_quiz, name='timed_quiz'),
    path('quiz/', views.quiz_list, name='quiz_list'),
    path('quiz/create/', views.quiz_create, name='quiz_create'),
    path('quiz/<int:pk>/update/', views.quiz_update, name='quiz_update'),
    path('quiz/<int:pk>/delete/', views.quiz_delete, name='quiz_delete'),
    
]
