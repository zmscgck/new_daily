#!/usr/bin/python

from django import forms

from . models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'company', 'quantity', 'character',
                  'start_time', 'end_time', 'days']
        labels = {'text': '工程名称'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['date_added', 'topic', 'worker',
                  'footage', 'rock', 'water', 'cement', 'text']
        labels = {'text': '工作内容'}
        widgets = {'text': forms.Textarea(attrs={'cols': 40})}
