from django.forms import ModelForm
from django import forms
from django.db import models
import uuid
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your models here.
class Employee(models.Model):
    class TestEnum(models.IntegerChoices):
        ZERO = 0
        ONE = 1

    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20, default="", blank=False)
    last_name = models.CharField(max_length=20, default="", blank=False)
    token_id = models.CharField(max_length=256, unique=True, default=uuid.uuid4)
    testhoge = models.IntegerField(choices=[(0, "Zero"), (1, "One")], null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "employee"

    @staticmethod
    def bulk_upsert(employees, batch_size):
        columns = [
            field.name
            for field in Employee._meta.get_fields()
            if field.name != "token_id"
            and field.name != "employee_id"
            and not isinstance(field, models.ManyToManyRel)
        ]

        Employee.objects.bulk_create(
            employees,
            batch_size,
            update_conflicts=True,
            unique_fields=["token_id"],
            update_fields=columns,
        )


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["first_name", "last_name"]

    @staticmethod
    def of(employee_id):
        employee = get_object_or_404(Employee, pk=employee_id)
        return EmployeeForm(instance=employee)

    @staticmethod
    def save(request, employee_id=None):
        form = (
            EmployeeForm(
                request.POST, instance=get_object_or_404(Employee, pk=employee_id)
            )
            if (employee_id)
            else EmployeeForm(request.POST)
        )
        return super(EmployeeForm, form).save()

    @staticmethod
    def delete(employee_id):
        employee = Employee.objects.get(pk=employee_id)
        return employee.delete()


class EmployeeSearchForm(forms.Form):
    first_name = forms.CharField(label="first_name", required=False)
    last_name = forms.CharField(label="last_name", required=False)

    def get_employees(self, page: int = 1, count: int = 5):
        employees = (
            Employee.objects.filter(
                first_name__contains=self.data["first_name"],
                last_name__contains=self.data["last_name"],
            )
            if self.data
            else Employee.objects.all()
        ).order_by("first_name", "last_name")

        paginator = Paginator(employees, count)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        return page_obj
