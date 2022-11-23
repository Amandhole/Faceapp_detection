from django.db import models
from picklefield.fields import PickledObjectField

# Table for admin registration
class AdminUserMaster(models.Model):
    Admin_Name = models.CharField(max_length=50, null=True, blank=True)
    Admin_username = models.CharField(max_length=50, null=True, blank=True)
    Admin_password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Admin_Name



#Table for employee registration
class EmployeeUserMaster(models.Model):
    fk_Admin_user = models.ForeignKey(AdminUserMaster, on_delete=models.CASCADE, null=True, blank=True)
    Employee_Name = models.CharField(max_length=100, blank=True, default='')
    Employee_Number = models.CharField(max_length=30, blank=True, default='')
    Employee_Email = models.EmailField(blank=True, null=True)
    Employee_Department = models.CharField(max_length=100, blank=True, default='')
    Employee_Designation = models.CharField(max_length=100, blank=True, default='')
    
    def __str__(self):
        return self.Employee_Name



#Table for employee check in check out
class Employee_Check_In_Out(models.Model):
    fk_Employee_user = models.ForeignKey(EmployeeUserMaster, on_delete=models.CASCADE, null=True, blank=True)   
    # Employee_Id =  models.CharField(max_length=100, blank=True, default='')
    Attendance_Type = models.CharField(max_length=100, blank=True, default='')   # AttendanceType(CheckIn/Checkout),
    IP_Address = models.CharField(max_length=100, blank=True, default='')
    check_In_Created_date_time = models.DateTimeField(null=True, blank=True)
    check_out_Created_date_time = models.DateTimeField(null=True, blank=True)
  

class Dummy(models.Model):
    image = models.FileField(upload_to='dummy_image/', null=True, blank=True)


class Employee_Table(models.Model):
    employee_id = models.CharField(max_length=250, null=True, blank=True)
    # image = models.FileField(null=True, blank=True, upload_to="local_workers/")
    pickle_obj = PickledObjectField(null=True, blank=True)
