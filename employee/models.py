from django.db import models
from django.core.validators import MinLengthValidator

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='USA')

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}"

class StaffBase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_joined = models.DateField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff')
    
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
