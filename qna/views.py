from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Question, Answer
from django.http import JsonResponse
import json
import pdb


class QuizView(TemplateView):
    template_name = "qna/index.html"


answers_array = []


def answers(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        answer = data.get("answer")
        answers_array.append(answer)
        pdb.set_trace()
        return JsonResponse({"status": 200})
