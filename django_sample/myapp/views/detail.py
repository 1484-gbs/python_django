from django.shortcuts import redirect, render
from django.views import View
from myapp.forms.employee import EmployeeForm


class DetailView(View):
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
