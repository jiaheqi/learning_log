from django.contrib import admin
from .models import Topic,Entry

# Register your models here.
admin.site.register(Topic)  # django通过管理网站管理模型
admin.site.register(Entry)