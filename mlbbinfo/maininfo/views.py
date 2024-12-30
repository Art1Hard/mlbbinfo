from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.template.defaultfilters import upper

from .models import Hero

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Герои", "url_name": "hero"},
    {"title": "Линии", "url_name": "line"},
    {"title": "Рассы", "url_name": "rase"},
    # {"title": "Обратная связь", "url_name": "contact"},
    # {"title": "Добавить статью", "url_name": "add_post"},
    # {"title": "Войти", "url_name": "login"},
]

roles_db = [
    {"id": 1, "name": "Маг"},
    {"id": 2, "name": "Убийца"},
    {"id": 3, "name": "Боец"},
    {"id": 4, "name": "Танк"},
    {"id": 5, "name": "Стрелок"},
    {"id": 6, "name": "Поддержка"},
]


def index(request):
    posts = Hero.published.all()
    data = {"title": "Всё о героях Mobile Legends", "posts": posts}
    return render(request, "maininfo/index.html", context=data)


def about(request):
    data = {"title": "О сайте mlbbinfo"}
    return render(request, "maininfo/about.html", context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Hero, slug=post_slug)
    data = {"title": post.title, "post": post}
    return render(request, "maininfo/post.html", context=data)


def heroes(request):
    return HttpResponse("dssda")


def lines(request):
    return HttpResponse("dssda")


def rases(request):
    return HttpResponse("dssda")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
