from django.contrib import admin
from .models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
    # list_display = []
    # list_filter = []
    # search_fields = []


# admin.site.register(Question)
# admin.site.register(Choice)
