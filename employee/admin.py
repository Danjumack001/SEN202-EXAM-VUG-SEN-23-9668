from django.contrib import admin
from .models import Manager, Intern, Address
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'postal_code')
    search_fields = ('street', 'city', 'postal_code')
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'has_company_card', 'address')
    list_filter = ('department', 'has_company_card', 'address')
    raw_id_fields = ('address',)
@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mentor', 'internship_end', 'address')
    list_filter = ('mentor', 'address')
    raw_id_fields = ('mentor', 'address',)
