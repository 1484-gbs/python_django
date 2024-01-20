from django.forms import ModelForm
from api.models.employee import Employee

from django.shortcuts import get_object_or_404


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
