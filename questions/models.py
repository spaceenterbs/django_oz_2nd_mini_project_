from django.db import models
from common.models import CommonModel


# class Question(models.Model):
class Question(CommonModel):
    question_a = models.BooleanField(
        default=False,
        help_text="첫 번째 질문입니다.",
    )
    question_b = models.BooleanField(
        default=False,
        help_text="두 번째 질문입니다.",
    )

    def __str__(self):
        return self.name  # f"{self.pk}번 질문"

    # 모델이 빈 데이터베이스. 쓰이는 데이터를 논의해야 한다. 데이터베이스에 저장해야 될 데이터를 논의해야 한다.
    # 대시보드에서 get, all, count 등 다양한 메소드를 요청할 수 있다.
    # serializer가 json 형태를 이해할 수 있게 바꿔줌; 파이썬이. json의 키값들이 연결된다.
