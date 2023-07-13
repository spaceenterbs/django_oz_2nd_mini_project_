from django.db import models
from common.models import CommonModel
from questions.models import Question, Choice


class Answer(models.Model):
    session_id = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)


class Result(models.Model):
    session_id = models.CharField(max_length=255)
    mbti_type = models.CharField(max_length=4)


# # models.py
# class Answer(CommonModel):
#     # 사용자의 응답을 저장하는 모델입니다.
#     # session_id 필드는 사용자를 식별하기 위해 사용됩니다.
#     session_id = models.CharField(max_length=255)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.session_id}: {self.choice.text}"


# class Result(CommonModel):
#     # 테스트 결과를 저장하는 모델입니다.
#     session_id = models.CharField(max_length=255)
#     mbti_type = models.CharField(max_length=4)

#     def __str__(self):
#         return f"{self.session_id}: {self.mbti_type}"


# # class Result(models.Model):
# class Result(CommonModel):
#     result_a = models.BooleanField(
#         default=False,
#     )
#     result_b = models.BooleanField(
#         default=False,
#     )
#     # owner = models.ForeignKey("questions.Question", on_delete=models.CASCADE) or models.SET_NULL
#     """ ForeignKey는 다른 모델의 """

#     # class Perk(CommonModel):

#     # """What is included on an Experiences"""

#     # name = models.CharField(
#     #     max_length=100,
#     # )

#     def __str__(self):
#         return self.name
