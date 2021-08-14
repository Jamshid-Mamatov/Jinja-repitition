from django import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import context, loader
# Create your views here.
def index(request):
    
    questions=Question.objects.order_by('-pub_date')[:]
    
    context={
        'questions':questions
    }

    return render(request,'formapp/index.html',context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)