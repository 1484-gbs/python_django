from django.shortcuts import redirect
from myapp.views.abstract_login_view import AbstractLoginRequiredView
from myapp.models.employee import EmployeeForm
import logging

logger = logging.getLogger("development")


class DeleteView(AbstractLoginRequiredView):
    def get(self, request, *args, **kwargs):
        EmployeeForm.delete(employee_id=kwargs["employee_id"])
        return redirect("index")


delete = DeleteView.as_view()
