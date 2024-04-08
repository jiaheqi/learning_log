from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from learning_logs.forms import TopicForm, EntryForm
from learning_logs.models import Topic, Entry


# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')  # 函数render()，它根据视图提供的数据渲染响应


@login_required
def topics(request):
    """显示所有主题"""
    # topics = Topic.objects.order_by('date_added')
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')  # 只允许用户访问属于自己的主题
    context = {'topics': topics}  # 定义一个将发送给模板的上下文。上下文是一个字典，其中的键是将在模板中用来访问数据的名称，而值是要发送给模板的数据。
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题的所有条目"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner!=request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')  # 横线表示降序排列
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':  # 如果不是post而是get请求，那么提交空表单
        form = TopicForm()  # 建一个TopicForm实例，将其赋给变量form，再通过上下文字典context将这个表单发送给模板
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():  # 方法is_valid()核实用户填写了所有必不可少的字段（表单字段默认都是必不可少的），且输入的数据与要求的字段类型一致
            # form.save()  # 将表单中的数据写入数据库
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')  # 函数redirect将视图名作为参数，并将用户重定向到这个视图
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)  # 无论是用户刚进入new_topic页面还是提交的表单数据无效，这些代码都将执行


@login_required
def new_entry(request, topic_id):
    """添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)  # ommit=False，让Django创建一个新的条目对象，并将其赋给new_entry，但不保存到数据库中
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)  # 两个参数：要重定向到的视图和要给视图函数提供的参数
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner!=request.user:
        raise Http404
    if request.method != 'POST':
        # 初次请求，回显当前条目
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,
                         data=request.POST)  # 传递实参instance=entry和data=request.POST，让Django根据既有条目对象创建一个表单实例
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
