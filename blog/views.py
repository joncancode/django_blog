# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>home!</h1>')

def about(request):
    return HttpResponse('<h1>about!</h1>')
