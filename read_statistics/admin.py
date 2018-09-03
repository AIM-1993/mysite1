from django.contrib import admin
from .models import ReadNum
# Register your models here.

@admin.register(ReadNum)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')
