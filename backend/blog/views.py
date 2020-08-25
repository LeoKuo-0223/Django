from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogList(ListView):  # Add
    model = Blog  # Add
    template_name = 'blogList.html'  # Add
