#!/usr/bin/python
from django import forms
from . models import IMG


class IMGForm(forms.ModelForm):
    class Meta:
        model = IMG
        fields = ['img', 'company', 'name']
        labels = {'img': '图片名称'}
