from django.shortcuts import redirect, render
from django.views import View
from myapp.models.user import SignupForm


class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/signup.html", {"form": SignupForm()})

    def post(self, request, *args, **kwargs):
        form = SignupForm.execute(request)
        if form.is_valid():
            return redirect("index")
        else:
            return render(request, "myapp/signup.html", {"form": form})


signup = SignupView.as_view()
