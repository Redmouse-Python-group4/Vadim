# -*-coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentsForm
from comments.models import Comments
from .models import Article, Category
# Create your views here.


def index(request):
    latest_article_list = Article.objects.filter(is_active=True).order_by('-pub_date')[0:8]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'article/index.html', context)


def num_index(request, num):
    number = int(num)
    latest_article_list = Article.objects.filter(is_active=True).order_by('-pub_date')[number*8:number*8+8]
    last_page = Article.objects.filter(is_active=True).order_by('-pub_date')[number*8+8:number*8+16]
    def check(latest_article_list):
        number = {'back': int(num)-1, 'next': int(num)+1}
        if last_page:
            context = {"latest_article_list": latest_article_list, 'number': number}
            return render(request, 'article/num_index.html', context)
        else:
            if latest_article_list:
                context = {"latest_article_list": latest_article_list, 'number': number}
                return render(request, 'article/last_page.html', context)
            else:
                return render(request, 'article/404.html')
    return check(latest_article_list)


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id, is_active=True)
    comments = Comments.objects.filter(article=article_id, enable=True).order_by('-pub_date')
    count_comments = comments.count()
    form = CommentsForm()
    context = {'article': article, 'comments': comments,
    'count_comments': count_comments,
    'form': form,
    }
    return render(request, 'article/article.html', context)


def category(request, category_id):
    latest_article_list = Article.objects.filter(category_id=category_id, is_active=True).order_by('-pub_date')
    category = get_object_or_404(Category ,pk=category_id)
    context = {'latest_article_list': latest_article_list, 'category': category}
    return render(request, 'article/category.html', context)


def create_comments(request, article_id):
    article = Article.objects.get(pk=article_id)
    form = CommentsForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.article = article
        obj.author = request.user
        obj.save()
        return redirect('/article/%s#comments' % article.id)
    return redirect('/')
