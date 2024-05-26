from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import FAQ, Article


def index(request):
    """ A view to return the home page"""
    return render(request, "yoda_app/index.html")


def about(request):
    """ A view to return the about page"""
    return render(request, "yoda_app/about.html")


def contact(request):
    """ A view to return the contact page"""
    return render(request, "yoda_app/contact.html")


def privacy_policy(request):
    """ A view to return the privacy_policy page"""
    return render(request, "yoda_app/privacy_policy.html")


def faq(request):
    """ A view to return the FAQ page"""
    faqs = FAQ.objects.all()

    return render(request, "yoda_app/faq.html", {'faqs': faqs})


def knowledge(request):
    """ A view to return the knowledge sanctuary page"""
    articles = Article.objects.all()
    knowledge_url = reverse('knowledge')

    return render(request, "yoda_app/knowledge.html", {'articles': articles, 'knowledge_url': knowledge_url})


def article_detail(request, slug):
    """ A view to return the article detail page"""
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'yoda_app/article_detail.html', {'article': article})

