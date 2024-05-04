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
            ],
            form_kwargs=dict(has_item=[1, 4]),
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
        sample_formset = SampleFormset(
            data=request.POST,
            # 必要
            initial=[
                dict(cd=1, value="保有", name="fender"),
                dict(cd=2, value="保有", name="gibson"),
                dict(cd=3, value="保有", name="tokai"),
                dict(cd=4, value="保有", name="yairi"),
            ],
        )
        if sample_formset.is_valid():

            print(
                [
                    int(d["guitar"])
                    for d in sample_formset.cleaned_data
                    if d["guitar"] is not ""
                ]
            )

            return redirect("index")

        return render(
            request,
            "myapp/detail.html",
            {
                "form": EmployeeForm(request.POST),
                "sample_formset": sample_formset,
            },
        )


detail = DetailView.as_view()
