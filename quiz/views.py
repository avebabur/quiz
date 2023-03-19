from django.shortcuts import render
from .models import Question, Answer, Stats
from random import shuffle
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.core.paginator import Paginator

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def questions(request):
    questions = Question.objects.all()
    context  = {
        'questions': questions
    }
    return render(request, 'quiz/questions.html', context)
from django.core.paginator import Paginator
from django.shortcuts import render
"""
def my_view(request):
    queryset = MyModel.objects.all()
    paginator = Paginator(queryset, 10) # 10 items per page
    page = request.GET.get('page')
    data = paginator.get_page(page)
    return render(request, 'my_template.html', {'data': data})"""
def quiz(request):
    queryset = Question.objects.all()
    """paginator = Paginator(queryset, 1)
    page = request.GET.get('page')
    data = paginator.get_page(page)"""
    context = {
        'questions': queryset
    }
    return render(request, 'quiz/question.html', context)
def quiz_json(request):
    questions = []
    for q in Question.objects.all():
        answers = []
        for a in q.get_answers():
            answers.append(a.answer)
        questions.append({str(q): answers})
    return JsonResponse({
        'questions': questions
    })
def save_quiz_view(request):
    #print(request.POST)
    if is_ajax(request=request):
        questions = []
        data = request.POST
        data_ = dict(data.lists())
       
        data_.pop('csrfmiddlewaretoken')
        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(question=k)
            questions.append(question)
        print(questions)
        user = request.user
        score = 0
        multiplier = 100 / len(Question.objects.all())
        results = []
        correct_answer = None
        for q in questions:
            a_selected = request.POST.get(q.question)
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.answer:
                        if a.correct:
                            score += 1
                            correct_answer = a.answer
                    else:
                        if a .correct:
                            correct_answer = a.answer
                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
        score_ = score * multiplier
        print(len(Question.objects.all()))
        Stats.objects.create(user=user, correct=score_, overall=len(Question.objects.all()))
    return JsonResponse({'score': score_, 'results': results})
def stats(request):
    stats = Stats.objects.all()
    context = {
        'stats': stats
    }
    return render(request, 'quiz/stats.html', context)
"""def questions_start(request):
    quiz = Question.objects.all()
    questions = []
    for question in quiz:
        answers = []
        for a in question.get_answers():
            answers.append(a.answer)
        questions.append({str(question): answers})
    return JsonResponse({
        'data': questions
    })"""
"""def questions(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, per_page=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'quiz/questions.html', {'page_obj': page_obj})"""

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('questions')
        else:
            messages.error(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'registration/sign_in.html', context)

def sign_out(request):
    logout(request)
    return redirect('questions')

def sign_up(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('questions')
        else:
            messages.error(request, 'An error occured during registration')
    context = {
        'form': form
    }
    return render(request, 'registration/sign_up.html', context)