from django.forms import ModelForm
from django.db import models
import uuid

from django.shortcuts import get_object_or_404


# Create your models here.
class Employee(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20, default="", blank=False)
    last_name = models.CharField(max_length=20, default="", blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "employee"

    # def __str__(self):
    #     return ' '.join([self.employee_id, self.first_name, self.last_name, self.createdAt, self.updatedAt])

    # @staticmethod
    # def register(id, first_name, last_name):
    #     # e = get_object_or_404(Employee, pk=id)
    #     e = Employee()
    #     e.employee_id = id
    #     e.first_name = first_name
    #     e.last_name = last_name
    #     e.save()
    #     return e


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["first_name", "last_name"]

    @staticmethod
    def of(employee_id):
        employee = get_object_or_404(Employee, pk=employee_id)
        return EmployeeForm(instance=employee)
