from django.views import View
from two_factor.views.mixins import OTPRequiredMixin
from myapp.templatetags.task_exists import TASK_ID_SESSION_KEY


class AbstractLoginRequiredView(OTPRequiredMixin, View):

    def set_task_id_in_session(self, request, task_id):
        task_ids = request.session.get(TASK_ID_SESSION_KEY, [])
        task_ids.append(task_id)
        request.session[TASK_ID_SESSION_KEY] = task_ids
