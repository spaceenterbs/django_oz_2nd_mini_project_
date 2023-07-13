from django.db import models
from common.models import CommonModel


# class Result(models.Model):
class Result(CommonModel):
    result_a = models.BooleanField(
        default=False,
    )
    result_b = models.BooleanField(
        default=False,
    )
    # owner = models.ForeignKey("questions.Question", on_delete=models.CASCADE) or models.SET_NULL
    """ ForeignKey는 다른 모델의 """

    # class Perk(CommonModel):

    # """What is included on an Experiences"""

    # name = models.CharField(
    #     max_length=100,
    # )

    def __str__(self):
        return self.name
