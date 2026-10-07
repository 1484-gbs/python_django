from django.shortcuts import redirect, render
from django.views import View
from myapp.models.user import LoginForm
from two_factor.views import LoginView as TwoFactorLoginView


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("index")
        else:
            return render(request, "myapp/login.html", {"form": LoginForm()})

    def post(self, request, *args, **kwargs):
        form = LoginForm.execute(request)
        if form.is_valid():
            return redirect("index")
        else:
            return render(request, "myapp/login.html", {"form": form})


login = LoginView.as_view()


class CustomTwoFactorLoginView(TwoFactorLoginView):
    def render(self, form=None, **kwargs):
        # フォームが存在し、バインドされており、かつエラーがある場合
        if form and form.is_bound and not form.is_valid():
            current_step = self.steps.current
            print(current_step)
            match current_step:
                case TwoFactorLoginView.AUTH_STEP:
                    print("ログイン失敗")
                case TwoFactorLoginView.TOKEN_STEP:
                    print("token入力失敗")
                case TwoFactorLoginView.BACKUP_STEP:
                    print("バックアップコード入力失敗")
                case _:
                    print(f"不明なステップ '{current_step}' でエラーが発生しました")
            print(form.errors)

            # コンテキストを追加したい場合などの例
            # kwargs['custom_error_flag'] = True

        return super().render(form=form, **kwargs)

    def get_success_url(self):
        print("ログイン成功！")
        return super().get_success_url()


# from django.contrib.auth.signals import user_login_failed
# from django.dispatch import receiver


# @receiver(user_login_failed)
# def log_user_login_failed(sender, credentials, request, **kwargs):
#     username = credentials.get("username") or credentials.get("email")
#     print(f"ログイン失敗: ユーザー名={username}, IP={request.META.get('REMOTE_ADDR')}")
