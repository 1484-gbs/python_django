from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from myapp.models.employee import Employee, EmployeeForm
import logging

logger = logging.getLogger("development")


class DetailView(View):
    # Create your views here.
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "myapp/detail.html",
            {"form": EmployeeForm.of(kwargs["employee_id"])},
        )

    def post(self, request, *args, **kwargs):
        employee_id = kwargs["employee_id"]
        employee = get_object_or_404(Employee, pk=employee_id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect("index")

    def delete(self, request, *args, **kwargs):
        employee_id = kwargs["employee_id"]
        employee = get_object_or_404(Employee, pk=employee_id)
        employee.delete()
        return redirect("index")


detail = DetailView.as_view()
