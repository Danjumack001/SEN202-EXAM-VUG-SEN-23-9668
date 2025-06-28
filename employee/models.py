from django.db import models
from django.core.validators import MinLengthValidator

class StaffBase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_joined = models.DateField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
    def get_role(self):
        return "Staff"

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)
    
    def get_role(self):
        return f"Manager of {self.department} department"

class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='interns')
    internship_end = models.DateField()
    
    def get_role(self):
        mentor_name = f" ({self.mentor.first_name})" if self.mentor else ""
        return f"Intern ending {self.internship_end}, mentored by{mentor_name}"

