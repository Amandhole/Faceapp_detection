from django.contrib import admin
from .models import *
# Register your models here.


class AdminUserMasterClass(admin.ModelAdmin):
	list_display = ('id', 'Admin_Name', 'Admin_username', 'Admin_password')
admin.site.register(AdminUserMaster, AdminUserMasterClass)


class EmployeeUserMasterClass(admin.ModelAdmin):
	list_display = ('id', 'fk_Admin_user', 'Employee_Name','Employee_Number', 'Employee_Email', 'Employee_Department','Employee_Designation')
admin.site.register(EmployeeUserMaster, EmployeeUserMasterClass)


class Employee_Check_In_OutClass(admin.ModelAdmin):
	list_display = ('id', 'fk_Employee_user', 'Attendance_Type', 'IP_Address','check_In_Created_date_time', 'check_out_Created_date_time')
admin.site.register(Employee_Check_In_Out, Employee_Check_In_OutClass)

class DummyAdmin(admin.ModelAdmin):
	list_display = ('id', 'image')
admin.site.register(Dummy, DummyAdmin)


class Employee_TableAdmin(admin.ModelAdmin):
	list_display = ('id', 'employee_id', 'pickle_obj')
admin.site.register(Employee_Table, Employee_TableAdmin)
