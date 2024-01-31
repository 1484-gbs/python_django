from django.db import models

from myapp.models.employee import Employee


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
        origin = OriginEmployee.objects.db_manager("database2").all()
        employees = list(
            map(
                lambda o: Employee(first_name=o.first_name, last_name=o.last_name),
                origin,
            )
        )
        print(len(employees))
        for employee in employees:
            print(
                "_".join(
                    [str(employee.employee_id), employee.first_name, employee.last_name]
                )
            )
        # print(origin)
        Employee.objects.bulk_create(employees, 100)
