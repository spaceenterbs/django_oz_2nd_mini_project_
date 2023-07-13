from rest_framework.serializers import ModelSerializer
from .models import User


class Serializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"  # Model의 전체 field 가져옴
        # fields = ("question_0", "question_1") # 원하는 특징 field만 가져옴
        # exclude = ("question_0", "question_1") # 원하는 특징 field만 제외하고 가져옴
