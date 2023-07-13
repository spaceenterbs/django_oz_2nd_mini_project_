from rest_framework import serializers
from .models import Answer, Result


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


# class AnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Answer
#         fields = "__all__"


# class ResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Result
#         fields = "__all__"
