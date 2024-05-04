from django.shortcuts import redirect, render
from myapp.forms.custom_formset import SampleFormset
from myapp.views.abstract_login_view import AbstractLoginRequiredView
from myapp.models.employee import EmployeeForm

import logging

logger = logging.getLogger("development")


class DetailView(AbstractLoginRequiredView):
    def get(self, request, *args, **kwargs):
        sample_formset = SampleFormset(
            initial=[
                dict(cd=1, value="保有", name="fender"),
                dict(cd=2, value="保有", name="gibson"),
                dict(cd=3, value="保有", name="tokai"),
                dict(cd=4, value="保有", name="yairi"),
            ]
        )
        return render(
            request,
            "myapp/detail.html",
            {
                "form": EmployeeForm.of(kwargs["employee_id"]),
                "sample_formset": sample_formset,
            },
        )

    def post(self, request, *args, **kwargs):
        EmployeeForm.save(request=request, employee_id=kwargs["employee_id"])
        return redirect("index")


detail = DetailView.as_view()
