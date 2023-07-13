from django.db import models
from common.models import CommonModel


class Question(models.Model):
    text = models.CharField(max_length=255)


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name="choices", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255)
    mbti_type = models.CharField(max_length=1)


# class Question(CommonModel):
#     # 각 문항을 나타내는 모델입니다.
#     # 예를 들어, "당신은 주로 외향적입니다 vs 내향적입니다"와 같은 문항이 될 수 있습니다.
#     text = models.CharField(max_length=255)

#     # option_a = '01'
#     # option_b = '02'

#     # options = [
#     #     (option_a, 'option_a'),
#     #     (option_b, 'option_b'),
#     # ]

#     # option_field = models.CharField(max_length=2, choices=options, null=True, blank=True)

#     def __str__(self):
#         return self.text


# class Choice(models.Model):
#     # 각 문항에 대한 선택지를 나타내는 모델입니다.
#     # 각 선택지는 MBTI의 어떤 요소에 관련이 있는지 표시해야 합니다 (예: "I" 또는 "E").
#     question = models.ForeignKey(
#         Question, related_name="choices", on_delete=models.CASCADE
#     )
#     text = models.CharField(max_length=255)
#     mbti_type = models.CharField(max_length=1)

#     def __str__(self):
#         return self.text


# # class Question(models.Model):
# class Question(CommonModel):
#     text = models.BooleanField(
#         default=False,
#         help_text="첫 번째 질문입니다.",
#     )
#     question_b = models.BooleanField(
#         default=False,
#         help_text="두 번째 질문입니다.",
#     )

#     def __str__(self):
#         return self.name  # f"{self.pk}번 질문"

#     # 모델이 빈 데이터베이스. 쓰이는 데이터를 논의해야 한다. 데이터베이스에 저장해야 될 데이터를 논의해야 한다.
#     # 대시보드에서 get, all, count 등 다양한 메소드를 요청할 수 있다.
#     # serializer가 json 형태를 이해할 수 있게 바꿔줌; 파이썬이. json의 키값들이 연결된다.
