from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from myapp.models.employee import Employee
# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        # return HttpResponse("hello.")
        return render(request, 
                    "myapp/index.html", 
                    {"employees": employees}
                )

index = IndexView.as_view()