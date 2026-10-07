from django.urls import include, path
from two_factor.urls import BackupTokensView, DisableView, urlpatterns as tf_urls
from django.core.exceptions import PermissionDenied

from myapp.views.login import CustomTwoFactorLoginView
from . import views


# mfaバックアップコードを管理者のみ有効
class DisabledBackupTokensView(BackupTokensView):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_authenticated and request.user.is_staff):
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


# mfa無効化を全ユーザー無効
class DisabledDisableView(DisableView):
    def dispatch(self, request, *args, **kwargs):
        raise PermissionDenied()


urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<uuid:employee_id>/", views.detail, name="detail"),
    path("delete/<uuid:employee_id>/", views.delete, name="delete"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("account/login/", CustomTwoFactorLoginView.as_view(), name="two_factor_login"),
    path(
        "account/two_factor/backup/tokens/",
        DisabledBackupTokensView.as_view(),
        name="backup_tokens",
    ),
    path(
        "account/two_factor/disable/",
        DisabledDisableView.as_view(),
        name="disable_tokens",
    ),
    path("", include(tf_urls)),
]
