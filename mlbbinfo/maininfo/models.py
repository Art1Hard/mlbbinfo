from django.db import models
from django.urls import reverse


class Line(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hero(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="заголовок")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="адрес страницы"
    )
    lines = models.ManyToManyField(Line, related_name="heroes")
    content = models.TextField(blank=True, verbose_name="описание")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="время обновления")
    is_published = models.BooleanField(default=True, verbose_name="опубликован?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "героя"
        verbose_name_plural = "герои"
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
