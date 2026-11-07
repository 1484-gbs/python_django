# myapp/templatetags/session_tags.py
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_session(context, key, default=None):
    request = context.get("request")
    if request and hasattr(request, "session"):
        return request.session.get(key, default)
    return default
