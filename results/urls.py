from django.urls import path
from .views import AnswerCreate, ResultCreate

app_name = "results"

urlpatterns = [
    path("answer/", AnswerCreate.as_view(), name="answer_create"),
    path("result/", ResultCreate.as_view(), name="result_create"),
]
