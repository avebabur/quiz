from django.urls import path
from .views import sign_in, sign_out, sign_up, questions, quiz, quiz_json, save_quiz_view, stats


urlpatterns = [
    path('', questions, name='questions'),
    path('login/', sign_in, name='sign in'),
    path('register/', sign_up, name='sign up'),
    path('logout/', sign_out, name='sign out'),
    #path('start/', questions_start, name='questions start'),
    #path('smth/', smth, name='smth'),
    path('quiz/', quiz, name='quiz'),
    path('quiz/json/', quiz_json, name='quiz_json'),
    path('quiz/jsson/', save_quiz_view, name='quiz_jsson'),
    path('stats/', stats, name='stats')
]