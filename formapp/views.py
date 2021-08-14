from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Question

# Create your views here.
def index(request):
    
    questions=Question.objects.order_by('-pub_date')[:]
    
    context={
        'questions':questions
    }

    return render(request,'formapp/index.html',context)

def detail(request, question_id):

    try:
        question=Question.objects.get(pk=question_id)
        
    except Question.DoesNotExist:
        print('except')
        raise Http404("question doesn't exist")

    context={
        'question':question
    }

    return render(request,'formapp/detail.html',context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)