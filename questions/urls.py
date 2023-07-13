from django.urls import path
from .views import QuestionList

app_name = "questions"

urlpatterns = [
    path("list/", QuestionList.as_view(), name="question_list"),
    # Add more paths for other views if needed
]
