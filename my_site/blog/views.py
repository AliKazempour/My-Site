from django.shortcuts import render


def starting_page(request):
    return render(request, "blog/start_page.html")


def post(request):
    return render(request, "blog/all_posts.html")


def post_detail(request,slug):
    return render(request, "blog/post-detail.html")
