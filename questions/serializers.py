from rest_framework import serializers
from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


# class ChoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Choice
#         fields = "__all__"


# class QuestionSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True, read_only=True)

#     class Meta:
#         model = Question
#         fields = "__all__"


# from rest_framework.serializers import ModelSerializer
# from .models import User


# class Serializer(ModelSerializer):
#     class Meta:
#         model = Feed
#         fields = "__all__"  # Model의 전체 field 가져옴
#         # fields = ("question_0", "question_1") # 원하는 특징 field만 가져옴
#         # exclude = ("question_0", "question_1") # 원하는 특징 field만 제외하고 가져옴
