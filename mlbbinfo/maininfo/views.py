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

data_db = [
    {
        "id": 1,
        "title": "клинт",
        "lines": ["золото"],
        "content": """Персонаж клинт имеет очень хорошую пассивку помогающая наносить повышенный критический урон помогающий пережить всё что готовит мне бабушка и не только клинт может многое!""",
        "is_published": True,
    },
    {
        "id": 2,
        "title": "джой",
        "lines": ["лес"],
        "content": """Персонаж клинт имеет очень хорошую пассивку помогающая наносить повышенный критический урон помогающий пережить всё что готовит мне бабушка и не только клинт может многое!""",
        "is_published": True,
    },
    {
        "id": 3,
        "title": "альфа",
        "lines": ["лес", "опыт"],
        "content": """Персонаж клинт имеет очень хорошую пассивку помогающая наносить повышенный критический урон помогающий пережить всё что готовит мне бабушка и не только клинт может многое!""",
        "is_published": True,
    },
    {
        "id": 4,
        "title": "кагура",
        "lines": ["мид"],
        "content": """Персонаж клинт имеет очень хорошую пассивку помогающая наносить повышенный критический урон помогающий пережить всё что готовит мне бабушка и не только клинт может многое! Оказывается не только""",
        "is_published": True,
    },
    {
        "id": 5,
        "title": "ланселот",
        "lines": ["лес"],
        "content": """Ланселот один из самых сильных убийц в игре. У него есть острая шпага а некоторые скилы помогают ланселоту уворачиваться от контроля ударов и так далее но только один раз пока скилы не перезарядятся""",
        "is_published": True,
    },
    {
        "id": 6,
        "title": "кармилла",
        "lines": ["роум"],
        "content": """Кармилла обладает хорошей танковкой, вампиризмом и уроном. Совокупность этих вакторов делает её хорошим героем в ранней и поздней стадии игры вот такие вот пироги. Что не сделаешь ради сиси блин!!!""",
        "is_published": True,
    },
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
    posts = Hero.objects.filter(is_published=1)
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
