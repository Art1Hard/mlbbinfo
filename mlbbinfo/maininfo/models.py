from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Line(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("line", kwargs={"line_slug": self.slug})


class BO(models.Model):
    price = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.price}"


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Hero(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="заголовок")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="адрес страницы"
    )
    lines = models.ManyToManyField(Line, related_name="heroes", db_index=True)
    bo = models.ForeignKey(
        BO, on_delete=models.PROTECT, related_name="heroes", db_index=True
    )
    content = RichTextField(blank=True, verbose_name="описание")
    views = models.PositiveIntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="время обновления")
    is_published = models.BooleanField(default=False, verbose_name="опубликован?")

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "героя"
        verbose_name_plural = "герои"
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
