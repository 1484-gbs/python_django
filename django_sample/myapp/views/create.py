from django.shortcuts import redirect, render
from myapp.views.abstract_login_view import AbstractLoginRequiredView
from myapp.models.employee import EmployeeForm


class CreateView(AbstractLoginRequiredView):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/detail.html", {"form": EmployeeForm()})

    def post(self, request, *args, **kwargs):
        EmployeeForm.save(request=request)
        return redirect("index")


create = CreateView.as_view()
