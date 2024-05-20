from django.contrib import admin

from .models import RandomQuiz

# Register your models here.

# 관리자 패널에서 퀴즈의 목록을 보여줄 필드 설정

admin.site.register(RandomQuiz)
