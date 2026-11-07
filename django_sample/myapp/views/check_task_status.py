# myapp/views.py
from django.http import JsonResponse
from django_q.tasks import fetch
from django.contrib.auth.decorators import login_required

from myapp.templatetags.task_exists import TASK_ID_SESSION_KEY


@login_required
def check_task_status(request):

    status = "processing"

    task_ids = request.session.get(TASK_ID_SESSION_KEY, [])
    new_task_ids = []

    if not task_ids:
        return JsonResponse({"status": "no_task"})

    successful_tasks = []
    error_tasks = []

    for task_id in task_ids:
        print(task_id)
        task = fetch(task_id)
        if not task:
            # タスクがまだ実行待ち、または見つからない場合
            new_task_ids.append(task_id)
            continue

        if task.success:
            # タスクが成功した場合
            successful_tasks.append(task.name)
        else:
            # タスクが失敗した場合
            error_tasks.append(str(task.result))

    result_dict = {}

    if len(successful_tasks) > 0:
        status = "continue"
        result_dict["filename"] = ",".join(successful_tasks)

    if len(error_tasks) > 0:
        status = "continue"
        result_dict["error"] = ",".join(error_tasks)

    if len(new_task_ids) == 0:
        status = "completed"

    print(status)
    print(new_task_ids)
    request.session[TASK_ID_SESSION_KEY] = new_task_ids
    print(result_dict)
    return JsonResponse({"status": status, "result": result_dict})
