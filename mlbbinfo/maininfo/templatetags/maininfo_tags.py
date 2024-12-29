from django import template
import maininfo.views as views

register = template.Library()


@register.simple_tag()
def get_menu_links():
    return views.menu


@register.inclusion_tag("maininfo/includes/menu.html")
def show_menu(request):
    return {"menu": views.menu, "request": request}
