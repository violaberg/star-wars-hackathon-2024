from django.shortcuts import render
from django.contrib import messages

from .models import FAQ


def index(request):
    """ A view to return the home page"""
    return render(request, "yoda_app/index.html")


def about(request):
    """ A view to return the about page"""
    return render(request, "yoda_app/about.html")


def faq(request):
    """ A view to return the FAQ page"""
    faqs = FAQ.objects.all()

    return render(request, "yoda_app/faq.html", {'faqs': faqs})