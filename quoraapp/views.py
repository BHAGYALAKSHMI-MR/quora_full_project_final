from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm, QuestionForm, AnswerForm
from .models import Question, Answer
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})


@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'ask_question.html', {'form': form})


@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all().order_by('-created_at')
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })


@login_required
def like_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.user in question.likes.all():
        question.likes.remove(request.user)
    else:
        question.likes.add(request.user)
    return redirect('question_detail', pk=question.id)


@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return redirect('question_detail', pk=answer.question.id)



def custom_logout(request):
    logout(request)  # logs out the user
    return redirect('home')  # redirects to homepage

@login_required
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    if request.user != question.author:
        return HttpResponseForbidden("You are not allowed to delete this question.")
    
    if request.method == 'POST':
        question.delete()
        return redirect('home')
    
    return render(request, 'confirm_delete.html', {'question': question})
