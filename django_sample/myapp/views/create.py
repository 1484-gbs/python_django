from django.shortcuts import redirect, render
from myapp.views.check_task_status import RUNNING_TASK_ID
from myapp.views.abstract_login_view import AbstractLoginRequiredView
from myapp.models.employee import EmployeeForm
from django_q.tasks import async_task
from django.contrib import messages
import uuid
import secrets


class CreateView(AbstractLoginRequiredView):
    def get(self, request, *args, **kwargs):
        return render(request, "myapp/detail.html", {"form": EmployeeForm()})

    def post(self, request, *args, **kwargs):
        EmployeeForm.save(request=request)
        task_name = f"task_{uuid.uuid4()}_{secrets.token_hex(2)}"
        task_id = async_task(
            test_heavy, q_options={"task_name": task_name}
        )  # 非同期で重い処理を実行
        print(f"task_id: {task_id}")
        messages.success(
            request,
            f"社員情報を登録しました。重い処理を非同期で実行中です。時間がたっても作成されていない場合は、管理者に[{task_name}]をあわせて問い合わせてください。",
        )
        request.session[RUNNING_TASK_ID] = task_id
        return redirect("index")


import time


def test_heavy():
    print(f"ヘビーな処理を開始します")
    # 重い処理をシミュレート
    time.sleep(10)
    print(f"ヘビーな処理を終えました")


create = CreateView.as_view()
