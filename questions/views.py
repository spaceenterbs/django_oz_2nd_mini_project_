from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# from django.shortcuts import render
# from django.http import HttpResponse


# def say_hello(request):
#     return HttpResponse("hello!!!")
