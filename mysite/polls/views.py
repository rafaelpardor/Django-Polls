from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, }
    # request, template_name, context=None, content_type=None, status=None, using=None
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)


def results(request, question_id):
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)
