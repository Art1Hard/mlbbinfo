from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.template.defaultfilters import capfirst

from .models import Hero, Line

menu = [
    {"title": "Герои", "url_name": "hero"},
    # {"title": "Линии", "url_name": "line"},
    # {"title": "Рассы", "url_name": "rase"},
    {"title": "Гайды", "url_name": "about"},
    {"title": "Поддержать проект", "url_name": "rase"},
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
    data = {
        "title": """Место, где ты найдёшь <span>ВСЁ</span> 
                    об игре Mobile Legends"""
    }
    return render(request, "maininfo/index.html", context=data)


def about(request):
    data = {"title": "О сайте mlbbinfo"}
    return render(request, "maininfo/about.html", context=data)


def updateViews(request, post):
    session_key = f"viewed_post_{post.pk}"
    if not request.session.get(session_key, False):
        post.views += 1
        post.save(update_fields=["views"])
        request.session[session_key] = True  # Помечаем пост как просмотренный


def show_post(request, post_slug):
    post = get_object_or_404(Hero, slug=post_slug)
    updateViews(request, post)
    data = {"title": post.title, "post": post}
    return render(request, "maininfo/post.html", context=data)


def heroes(request):
    posts = Hero.published.all()
    data = {"title": "Все герои Mobile Legends", "posts": posts}
    return render(request, "maininfo/heroes.html", context=data)


def show_line(request, line_slug):
    line = get_object_or_404(Line, slug=line_slug)
    posts = Hero.published.filter(lines=line)
    data = {"title": capfirst(change_line_end(line)), "posts": posts}
    return render(request, "maininfo/heroes.html", context=data)


def change_line_end(line):
    line_name = "линия"
    if line.name == "золото":
        return f"{line_name} золота"
    if line.name == "мид":
        return f"средняя {line_name}"
    return f"{line_name} {line.name}а"


def rases(request):
    return HttpResponse("dssda")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
