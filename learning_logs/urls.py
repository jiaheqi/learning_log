"""定义learning_logs的URL模式"""
from django.urls import path

from learning_logs import views

app_name = 'learning_logs'  # 变量app_name让Django能够将这个urls.py文件同项目内其他应用程序中的同名文件区分开来
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 第一部分让Django查找在基础URL后包含单词topics的URL，第二部分(/<int:topic_id>/)与包含在两个斜杠内的整数匹配，并将这个整数存储在一个名为topic_id的实参中
    # 用于添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加条目的页面
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    # 用于编辑条目的页面
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry')

]
