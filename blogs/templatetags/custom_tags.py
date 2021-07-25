from django import template
from blogs.models import Blog

register = template.Library()

@register.simple_tag(name="blogs")
def all_categories():
    return Blog.objects.all()