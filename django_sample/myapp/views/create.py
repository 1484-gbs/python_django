from django.shortcuts import redirect, render
from django.views import View
from myapp.forms.employee import EmployeeForm


class CreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/detail.html", {"form": EmployeeForm()})

    def post(self, request, *args, **kwargs):
        EmployeeForm.save(request=request)
        return redirect("index")


create = CreateView.as_view()
