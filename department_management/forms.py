from django import forms

from .models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_code', 'department_name', 'department_head', 'office_location', 'date_established']
