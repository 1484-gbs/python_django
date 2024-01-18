from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from myapp.models.employee import Employee, EmployeeForm
import logging

logger = logging.getLogger("development")


class CreateView(View):
    # Create your views here.
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/detail.html", {"form": EmployeeForm()})

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST)
        new_employee = form.save()
        # return redirect("detail", employee_id=new_employee.employee_id)
        return redirect("index")


create = CreateView.as_view()
