from django.contrib import admin
from .models import Answer, Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass
    # list_display = []
    # list_filter = []
    # search_fields = []


# admin.site.register(Answer)
# admin.site.register(Result)
