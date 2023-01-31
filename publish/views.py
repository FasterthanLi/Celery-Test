from django.shortcuts import render
from django.views import View
from django.http import Http404
from django.views.generic import DetailView
from .models import Post

class ViewPost(DetailView):
    model = Post
    template_name = 'post.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj is None:
            raise Http404("Poll does not exist")
        return obj
