from django.shortcuts import render
from datetime import date
from .models import Tag,Post,Author

all_posts = []


def get_date(post):
    return post['date']


def starting_page(request):
    lastest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "blog/start_page.html", {"posts": lastest_posts})


def post(request):
    all_posts = Post.objects.all().order_by()
    return render(request, "blog/all_posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    identified_post=next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html", {"post":identified_post})
