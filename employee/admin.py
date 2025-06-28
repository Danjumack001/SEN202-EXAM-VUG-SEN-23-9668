from django.contrib import admin
from .models import Manager, Intern

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'has_company_card')
    list_filter = ('department', 'has_company_card')

@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mentor', 'internship_end')
    list_filter = ('mentor',)

