from django.shortcuts import redirect
from django.views import View
from myapp.forms.employee import EmployeeForm


class DeleteView(View):
    def get(self, request, *args, **kwargs):
        EmployeeForm.delete(employee_id=kwargs["employee_id"])
        return redirect("index")


delete = DeleteView.as_view()
