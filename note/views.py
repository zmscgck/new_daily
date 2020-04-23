from django.shortcuts import render
from note.models import Topic, Entry
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from note.forms import TopicForm, EntryForm, EntryForm01
from django.contrib.auth.decorators import login_required
import django.utils.timezone as timezone
from django.contrib.auth.models import User, Group


# Create your views here.
def index(request):
    # 施工日报的主页
    return render(request, 'note/index.html')


@login_required
def new_daily(request):
    # 显示（所属单位）或登陆人新填写的施工日报
    user = request.user # 登陆账号人名字
        # group = user_group.objects(id=user_id)
    date_added = timezone.now()
    us = User.objects.get(username=user)
    user_id = us.id  # 登陆人的用户id
    gs = Group.objects.filter(user=user_id) # 登陆人所属群组
    if gs:
        entries = []
        for group in gs:
            entries += Entry.objects.filter(
        date_added=timezone.localtime().strftime("%F")
        ).filter(company=group).order_by('-date_added').order_by('-id')    
        entries = entries
        context = {'entries': entries, 'date_added': date_added}
    else:
        entries = Entry.objects.filter(
        date_added=timezone.localtime().strftime("%F")
        ).filter(recorder=user).order_by('-date_added').order_by('-id')
        context = {'entries': entries, 'date_added': date_added}
    return render(request, 'note/daily.html', context)



    entries = Entry.objects.filter(
        date_added=timezone.localtime().strftime("%F")
        ).order_by('-date_added').order_by('-id')
    context = {'entries': entries, 'date_added': date_added}
    return render(request, 'note/daily.html', context)


@login_required
def topics(request):
    # 显示管理单位的所有工程，如未设定归属单位，显示新建单位工程
    user = request.user  # 登陆人的名字
    us = User.objects.get(username=user)
    user_id = us.id  # 登陆人的用户id
    gs = Group.objects.filter(user=user_id) # 登陆人所属群组
    if gs :
        topics = []
        for group in gs:
            topics += Topic.objects.filter(company=group).order_by('-date_added').order_by('-id')
        context = {'topics': topics}
    else:
        topics = Topic.objects.filter(owner=user).order_by('-date_added').order_by('-id')
        context = {'topics': topics}
    return render(request, 'note/topics.html', context)


@login_required
def entries(request):
    # 显示全矿（所管理单位的）施工日报记录15条
    user = request.user  # 登陆人的名字
    us = User.objects.get(username=user)
    user_id = us.id  # 登陆人的用户id
    gs = Group.objects.filter(user=user_id) # 登陆人所属群组
    if gs :
        entries = []
        for group in gs:
            entries += Entry.objects.filter(company=group).order_by('-date_added').order_by('-id')[0:5]    
        entries = entries[0:15]
        context = {'entries': entries}
    else:
        entries = Entry.objects.filter(recorder=user).order_by('-date_added').order_by('-id')[0:5]    
        context = {'entries': entries}
    return render(request, 'note/entries.html', context)


@login_required
def new_topic(request):
    # 添加单位工程
    user = request.user
    ts = Topic.objects.all()
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
        #print("单位工程不能重复!")
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            text = new_topic.text
            for i in ts:
                if text == i.text:
                    # 如工程重复，清空重新填写
                    return HttpResponseRedirect(reverse('note:new_topic'))
            new_topic.owner = user
            new_topic.save()
            return HttpResponseRedirect(reverse('note:topics'))
    context = {'form': form}
    return render(request, 'note/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    '''在指定单位工程中添加施工日报'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm01()
    else:
        # post提交的数据，对数据进行处理
        form = EntryForm01(data=request.POST)
        # 判断单位工程是否填写重复！
        es = Entry.objects.filter(
            date_added=timezone.now().strftime("%F"))
        if form.is_valid:
            new_entry = form.save(commit=False)
            for i in es:
                if topic == i.topic:
                    # 如工程重复，清空重新填写
                    return HttpResponseRedirect(reverse(
                            'note:new_entry', args=[topic_id]))
            new_entry.topic = topic
            new_entry.recorder = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('note:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'note/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    '''编辑施工日报'''
    recorder = request.user
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # 确认请求的日报当前用户记录
    if entry.recorder != request.user:
        raise Http404
    if request.method != 'POST':
        # 初次请求，使用当前日报填充表单
        form = EntryForm01(instance=entry)
    else:
        # post提交的数据，对数据进行处理
        form = EntryForm01(request.POST)
        if form.is_valid:
            entry = form.save(commit=False)
            entry.recorder = recorder
            entry.id = entry_id
            entry.topic = topic
            entry.save()
            return HttpResponseRedirect(reverse('note:daily'))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'note/edit_entry.html', context)


@login_required
def new_entries(request):
    '''选择单位工程，添加施工日报'''
    date_added = timezone.now()
    recorder = request.user
    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()
    else:
        # post提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        # 判断单位工程是否填写重复！
        es = Entry.objects.filter(
            date_added=timezone.now().strftime("%F"))
        if form.is_valid:
            new_entry = form.save(commit=False)
            topic = new_entry.topic
            for i in es:
                if topic == i.topic:
                    # 如工程重复，清空重新填写
                    return HttpResponseRedirect(reverse('note:new_entries'))
            new_entry.recorder = recorder
            new_entry.date_added = date_added
            new_entry.save()
            form.save()
            return HttpResponseRedirect(reverse('note:daily'))
    context = {'form': form}
    return render(request, 'note/new_entries.html', context)
