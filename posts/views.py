# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def get_one_article(request, id):
    # Get article by it's ID
    article = get_object_or_404(Article, pk=id)
    context = {
        'article': article
    }
    return render(request, 'get_one_article.html', context)


def login(request):
    return render(request, 'login.html')