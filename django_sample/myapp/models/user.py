from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    @staticmethod
    def execute(request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

        return form


class LoginForm(AuthenticationForm):
    @staticmethod
    def execute(request):
        form = LoginForm(data=request.POST)
        if not form.is_valid():
            return form
        user = form.get_user()
        try:
            login(request, user)
        except:
            form.add_error(None, "LOGIN_ID、またはPASSWORDが違います。")

        return form


class LogoutForm:
    @staticmethod
    def execute(request):
        logout(request)
