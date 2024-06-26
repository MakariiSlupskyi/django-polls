from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    latest_qs = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_qs" : latest_qs}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, "polls/detail.html", {"question" : question})


def results(request, question_id):
    response = "You're looking at the result of qeustion"
    return HttpResponse(f"{response} {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on a question {question_id}")