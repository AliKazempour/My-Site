from typing import Any
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Tag, Post, Author
from django.views.generic import ListView,DetailView
from .models import Tag, Author, Post
from .forms import CommentForm

class StartingPageView(ListView):
    model = Post
    template_name = "blog/start_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by('-date')[:3]
        return context


class PostsView(ListView):
    model = Post
    template_name = "blog/all_posts.html"
    context_object_name = "all_posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    
    def get_context_data(self, ** kwargs):
        context = super().get_context_data(** kwargs)
        context["post_tags"]= self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context

