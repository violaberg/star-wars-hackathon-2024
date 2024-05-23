from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.views import generic, View

from .models import Post, Comment
from .models import FAQ


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(is_published=True)
    template_name = 'yoda_app/index.html'
    context_object_name = 'posts'


def faq(request):
    """ A view to return the FAQ page"""
    faqs = FAQ.objects.all()

    return render(request, "yoda_app/faq.html", {'faqs': faqs})