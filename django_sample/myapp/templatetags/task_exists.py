# myapp/templatetags/session_tags.py
from django import template

register = template.Library()

TASK_ID_SESSION_KEY = "task_ids"


@register.simple_tag(takes_context=True)
def task_exists(context, default=None):
    request = context.get("request")
    if request and hasattr(request, "session"):
        return len(request.session.get(TASK_ID_SESSION_KEY, [])) > 0
    return default
