from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from django.views.generic import ListView, CreateView, UpdateView
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


class BlogCreate(LoginRequiredMixin, CreateView):  # Add
    model = Blog  # Add
    fields = '__all__'  # Add
    template_name = 'form.html'  # Add

    def get_success_url(self):  # Add
        return reverse('BlogList')  # Add


class BlogUpdate(LoginRequiredMixin, UpdateView):  # Add
    model = Blog  # Add
    fields = '__all__'  # Add
    template_name = 'form.html'  # Add

    def get_success_url(self):  # Add
        return reverse('BlogList')  # Add
