from django.shortcuts import redirect
from myapp.views.abstract_login_view import AbstractLoginRequiredView
from myapp.models.user import LogoutForm


class LogoutView(AbstractLoginRequiredView):
    def post(self, request, *args, **kwargs):
        LogoutForm.execute(request)
        return redirect("login")


logout = LogoutView.as_view()
