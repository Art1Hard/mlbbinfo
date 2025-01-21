from django.urls import path, re_path, register_converter
from django.conf import settings
from django.conf.urls.static import static

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("posts/<slug:post_slug>/", views.show_post, name="post"),
    path("heroes/", views.heroes, name="hero"),
    path("heroes/lines/<slug:line_slug>/", views.show_line, name="line"),
    path("rases", views.rases, name="rase"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
