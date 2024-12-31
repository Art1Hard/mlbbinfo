from django import template
import maininfo.views as views
from maininfo.models import Line

register = template.Library()


@register.inclusion_tag("maininfo/includes/menu.html")
def show_menu(request):
    return {"menu": views.menu, "request": request}


@register.inclusion_tag("maininfo/includes/lines.html")
def show_lines():
    lines = Line.objects.all()
    return {"lines": lines}
