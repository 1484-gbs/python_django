from django.shortcuts import redirect, render
from myapp.views.abstract_login_view import AbstractLoginRequiredView
from myapp.models.employee import EmployeeForm
import logging

logger = logging.getLogger("development")


class DetailView(AbstractLoginRequiredView):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "myapp/detail.html",
            {"form": EmployeeForm.of(kwargs["employee_id"])},
        )

    def post(self, request, *args, **kwargs):
        EmployeeForm.save(request=request, employee_id=kwargs["employee_id"])
        return redirect("index")


detail = DetailView.as_view()
