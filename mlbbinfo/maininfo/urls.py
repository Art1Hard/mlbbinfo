from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("posts/<slug:post_slug>/", views.show_post, name="post"),
    path("heroes/", views.heroes, name="hero"),
    path("lines/<slug:line_slug>/", views.show_line, name="line"),
    path("rases", views.rases, name="rase"),
]
