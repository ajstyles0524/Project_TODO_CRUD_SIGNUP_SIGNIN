from django import forms
from employee_crud.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
