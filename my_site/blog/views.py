from typing import Any
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Tag, Post, Author
from django.views.generic import ListView, DetailView, View
from .models import Tag, Author, Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


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


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post-detail.html", context={
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        })

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        return render(request, "blog/post-detail.html", context={
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm
        })
