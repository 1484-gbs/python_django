from django.shortcuts import render
from django.views import View
from myapp.models.employee import Employee


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, "myapp/index.html", {"employees": Employee.objects.all()}
        )


index = IndexView.as_view()
