"""
定义users的url模式
"""
from django.urls import path, include

from users import views

app_name = 'users'  # 变量app_name让Django能够将这个urls.py文件同项目内其他应用程序中的同名文件区分开来
urlpatterns = [
    # 包含默认的身份认证url
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register')
]