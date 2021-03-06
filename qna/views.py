from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Question, Answer
from django.http import JsonResponse
import json
import pdb


class QuizView(TemplateView):
    template_name = "qna/index.html"


# answer_array is going to collect all user's answers
answers_array = []
correct_answers = [answer.text for answer in Answer.objects.filter(correct=True)]


def answers(request: dict):
    """
    Returns the score after the question has been answered
    """
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        answer = data.get("answer")
        answers_array.append(answer)
        score = len([item for item in correct_answers if item in answers_array])

        if len(answers_array) == len(Question.objects.all()):
            response = {"body": {"score": score}}
            return JsonResponse(data=response, status=200)
        else:
            return JsonResponse(data={"body": {"score": score}}, status=200)
