from django.contrib import admin

from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_code', 'department_name', 'department_head', 'office_location', 'date_established')
    search_fields = ('department_code', 'department_name', 'department_head', 'office_location')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
