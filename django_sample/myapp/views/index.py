from django.shortcuts import render
from myapp.views.abstract_login_view import AbstractLoginRequiredView
from myapp.models.employee import Employee


# Create your views here.
class IndexView(AbstractLoginRequiredView):
    def get(self, request, *args, **kwargs):
        return render(
            request, "myapp/index.html", {"employees": Employee.objects.all()}
        )


index = IndexView.as_view()
