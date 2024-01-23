from django.shortcuts import redirect, render
from django.views import View
from myapp.models.user import LoginForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/login.html", {"form": LoginForm()})

    def post(self, request, *args, **kwargs):
        form = LoginForm.execute(request)
        if form.is_valid():
            return redirect("index")
        else:
            return render(request, "myapp/login.html", {"form": form})


login = LoginView.as_view()
