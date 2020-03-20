from django.shortcuts import render
from note.models import Topic, Entry
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from note.forms import TopicForm, EntryForm, EntryForm01
from django.contrib.auth.decorators import login_required
import django.utils.timezone as timezone


# Create your views here.
def index(request):
    # 施工日报的主页
    return render(request, 'note/index.html')


@login_required
def new_daily(request):
    # 显示新填写的施工日报
    date_added = timezone.now()
    entries = Entry.objects.filter(owner=request.user).filter(
        date_added=timezone.now().strftime("%F")
        ).order_by('-date_added').order_by('-id')
    context = {'entries': entries, 'date_added': date_added}
    return render(request, 'note/daily.html', context)


def graph(request):
    # 施工图表
    disp = TopicAdmin.list_display
    sear = TopicAdmin.search_fields   # 搜索功能
    filt = TopicAdmin.list_filter   # 过滤器
    context = {'disp': disp, 'sear': sear, 'filt': filt}
    return render(request, 'note/graph.html', context)


@login_required
def topics(request):
    # 显示管理的所有单位工程
    topics = Topic.objects.order_by('-date_added').order_by('-id')
    context = {'topics': topics}
    return render(request, 'note/topics.html', context)


@login_required
def topic(request, topic_id):
    # 显示一个单位工程及施工日报
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的单位工程属于当前用户管理
    #if topic.owner != request.user:
    #    raise Http404
    entries = topic.entry_set.order_by('-date_added').order_by('-id')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'note/topic.html', context)


@login_required
def entries(request):
    # 显示管理工程的所有施工日报
    entries = Entry.objects.filter(owner=request.user).\
        order_by('-date_added').order_by('-id')[0:16]
    context = {'entries': entries}
    return render(request, 'note/entries.html', context)


@login_required
def new_topic(request):
    # 添加单位工程
    ts = Topic.objects.all()
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            text = new_topic.text
            for i in ts:
                if text == i.text:
                    form = TopicForm()  # 如工程重复，清空重新填写
                    return HttpResponseRedirect(reverse('note:new_topic'))
            #new_topic.owner = request.user
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
                    form = EntryForm()  # 如工程重复，清空重新填写
                    return HttpResponseRedirect(reverse(
                            'note:new_entry', args=[topic_id]))
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('note:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'note/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    '''编辑施工日报'''
    owner = request.user
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # 确认请求的日报当前用户记录
    #    raise Http404
    if request.method != 'POST':
        # 初次请求，使用当前日报填充表单
        form = EntryForm01(instance=entry)
    else:
        # post提交的数据，对数据进行处理
        form = EntryForm01(request.POST)
        if form.is_valid:
            entry = form.save(commit=False)
            entry.owner = owner
            entry.id = entry_id
            entry.topic = topic
            entry.save()
            return HttpResponseRedirect(reverse('note:daily'))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'note/edit_entry.html', context)


@login_required
def new_entries(request):
    '''选择单位工程，添加施工日报'''
    owner = request.user
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
                    form = EntryForm()  # 如工程重复，清空重新填写
                    return HttpResponseRedirect(reverse('note:new_entries'))
            new_entry.owner = owner
            new_entry.save()
            form.save()
            return HttpResponseRedirect(reverse('note:daily'))
    context = {'form': form}
    return render(request, 'note/new_entries.html', context)
