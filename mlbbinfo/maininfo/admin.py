from django.contrib import admin
from maininfo import models

admin.site.register(models.Line)
admin.site.register(models.BO)
admin.site.register(models.IntroSlide)


@admin.register(models.Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "time_update",
        "is_published",
    )  # Поля, отображаемые в списке
    search_fields = ("title",)  # Поля для поиска
    list_filter = (
        "time_update",
        "time_create",
    )  # Фильтры
    ordering = ("title",)  # Сортировка
    readonly_fields = ("views",)
