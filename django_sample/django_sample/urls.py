"""
URL configuration for django_sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from datetime import datetime
import secrets
from zoneinfo import ZoneInfo

from django.contrib import admin
from django.urls import include, path
from api.urls import router as api_router
from two_factor.admin import AdminSiteOTPRequired
from django.shortcuts import render
import logging
import traceback

logger = logging.getLogger()

# adminサイトにmfaを強制する
admin.site.__class__ = AdminSiteOTPRequired


def custom_500_view(request):
    # ユーザー情報やリクエスト情報の安全な取得（未認証やAttributeErrorに配慮）
    user = getattr(request, "user", "Anonymous/None")
    path = getattr(request, "path", "Unknown Path")
    method = getattr(request, "method", "Unknown Method")
    now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y%m%d-%H%M%S")
    error_id = f"e-{now}-{secrets.token_hex(2)}"
    # exc_info=True を渡すと、発生していた直前の例外トレースバックが自動でログに含まれる
    logger.error(
        f"[{error_id}] 500 Internal Server Error: [{method}] {path})",
        exc_info=True,
    )
    # # flush=True を指定してバッファリングを防ぎ、即座に出力させる
    # print(f"\n========== [500 ERROR: {error_id}] ==========", flush=True)
    # print(f"Method: {method}", flush=True)
    # print(f"Path:   {path}", flush=True)
    # print(f"Time:   {now}", flush=True)
    # print("---------- TRACEBACK ----------", flush=True)

    # # 発生していた例外のスタックトレースを標準エラー出力へ直接プリント
    # traceback.print_exc()

    # print("=================================\n", flush=True)

    # トレースバックを文字列として変数に代入
    # error_traceback = traceback.format_exc()

    return render(
        request,
        template_name="500.html",
        context={
            "error_id": error_id,
        },
        status=500,
    )


handler500 = custom_500_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("myapp/", include("myapp.urls")),
    path("myapp/api/", include(api_router.urls)),
]
