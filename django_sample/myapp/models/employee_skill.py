from django.db import models
import uuid

from myapp.models.employee import Employee
from myapp.models.skill import Skill


# Create your models here.
class EmployeeSkill(models.Model):

    employee_skill_id = models.BigIntegerField(primary_key=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="employee_skill"
    )
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        db_table = "employee_skill"
