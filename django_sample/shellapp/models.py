from django.db import models
from myapp.models.employee import Employee
from django.conf import settings
from django.core.paginator import Paginator


# Create your models here.
class OriginEmployee(models.Model):
    employee_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=20, default="", blank=False)
    last_name = models.CharField(max_length=20, default="", blank=False)
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
            employees = list(
                map(
                    lambda o: Employee(first_name=o.first_name, last_name=o.last_name),
                    obj_list,
                )
            )
            print(len(employees))
            for employee in employees:
                print(
                    "_".join(
                        [
                            str(employee.employee_id),
                            employee.first_name,
                            employee.last_name,
                        ]
                    )
                )

            Employee.objects.bulk_create(employees, settings.TRANSFER_BATCH_SIZE)
            print("bulk_create")
