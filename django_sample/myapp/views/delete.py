from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from myapp.models.employee import Employee, EmployeeForm
import logging

logger = logging.getLogger("development")


class DeleteView(View):
    def get(self, request, *args, **kwargs):
        Employee.delete(employee_id=kwargs["employee_id"])
        return redirect("index")


delete = DeleteView.as_view()
