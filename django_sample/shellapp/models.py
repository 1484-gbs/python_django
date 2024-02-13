from django.db import models
from django.forms import model_to_dict
from myapp.models.employee import Employee
from django.conf import settings
from django.core.paginator import Paginator


# Create your models here.
class OriginEmployee(models.Model):
    employee_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=20, default="", blank=False)
    last_name = models.CharField(max_length=20, default="", blank=False)
    token_id = models.CharField(max_length=256, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = "employee"

    @staticmethod
    def transfer():
        paginator = Paginator(
            OriginEmployee.objects.db_manager("database2")
            .all()
            .order_by("employee_id"),
            settings.TRANSFER_CHUNK_SIZE,
        )
        print(paginator.num_pages)

        for page_idx in range(1, paginator.num_pages + 1):
            obj_list = paginator.page(page_idx).object_list
            print(obj_list)
            employees = [Employee(**model_to_dict(o)) for o in obj_list]
            print(len(employees))
            for employee in employees:
                print(
                    "_".join(
                        [
                            str(employee.employee_id),
                            employee.first_name,
                            employee.last_name,
                            employee.token_id,
                        ]
                    )
                )

            Employee.bulk_upsert(employees, settings.TRANSFER_BATCH_SIZE)
            print("bulk_create")
