from rest_framework import generics
from .models import Answer, Result
from .serializers import AnswerSerializer, ResultSerializer


class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ResultCreate(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


# from django.shortcuts import render

# # Create your views here.
