# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

posts = [
    {
        'author': 'Jon',
        'title': 'blog post 1',
        'content': 'content for first post',
        'date_posted': 'Jan, 17, 2019'
    },
    {
        'author': 'Other guy',
        'title': 'blog post 2',
        'content': 'content for second post',
        'date_posted': 'Jan, 18, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
