from django.shortcuts import redirect, render
from myapp.views.abstract_login_view import AbstractLoginRequiredView
from myapp.models.employee import Employee, EmployeeSearchForm


# Create your views here.
class IndexView(AbstractLoginRequiredView):
    SESSION_KEY = "EmployeeSearchForm"

    def get(self, request, *args, **kwargs):
        form = (
            EmployeeSearchForm(self.request.session[self.SESSION_KEY])
            if self.SESSION_KEY in self.request.session
            else EmployeeSearchForm()
        )
        page_obj = form.get_employees(page=request.GET.get("page"))
        return self.__render(request, page_obj, form)

    def post(self, request, *args, **kwargs):
        form = EmployeeSearchForm(request.POST)
        if not form.is_valid():
            return self.__render(request, None, form)
        else:
            self.request.session[self.SESSION_KEY] = form.cleaned_data
            page_obj = form.get_employees()
            return self.__render(request, page_obj, form)
            # return redirect("index")

    def __render(self, request, page_obj, form):
        list = page_obj.object_list if page_obj else []

        return render(
            request,
            "myapp/index.html",
            {
                "employees": list,
                "form": form,
                "page_obj": page_obj,
            },
        )


index = IndexView.as_view()
