# myapp/views.py
from django.http import JsonResponse
from django_q.models import Task
from django.contrib.auth.decorators import login_required

RUNNING_TASK_ID = "running_task_id"


@login_required
def check_task_status(request):
    """セッションを元にタスクの状態を正しくチェックするAPI"""
    # 💡 明示的に SQLite からデータを参照させる
    task_id = request.session.get("running_task_id")

    # 1. セッションにタスクIDがない ＝ タスクが動いていない
    if not task_id:
        return JsonResponse({"status": "NONE"})

    # 2. SQLite からタスクオブジェクト自体を取得
    task = Task.get_task(task_id)

    # タスクデータ自体が見つからない場合もループを止める
    if task is None:
        if "running_task_id" in request.session:
            del request.session["running_task_id"]
        return JsonResponse({"status": "NONE"})

    # 3. タスクの完了判定 (success属性は完了時に True または False になる)
    # まだ実行中（またはキュー待機中）は success が None
    if task.success is None:
        return JsonResponse({"status": "PENDING"})

    # 4. タスクが完了した場合の処理
    # 完了したのでセッションからIDを削除
    if "running_task_id" in request.session:
        del request.session["running_task_id"]

    return JsonResponse(
        {
            "status": "COMPLETED",
            "success": task.success,  # 成功ならTrue, 失敗ならFalse
        }
    )
