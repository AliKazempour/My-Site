from django.shortcuts import render


def starting_page(request):
    return render(request, "blog/start_page.html")


def post(request):
    pass


def post_detail(request):
    pass
