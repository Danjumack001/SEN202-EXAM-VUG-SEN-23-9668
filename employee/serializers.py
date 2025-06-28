from rest_framework import serializers
from .models import Manager, Intern, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'state', 'postal_code', 'country']

class ManagerSerializer(serializers.ModelSerializer):
    address_details = AddressSerializer(source='address', read_only=True)
    
    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'date_joined', 
                'department', 'address', 'address_details']
        read_only_fields = ['has_company_card']

class InternSerializer(serializers.ModelSerializer):
    mentor_details = serializers.SerializerMethodField()
    address_details = AddressSerializer(source='address', read_only=True)
    
    class Meta:
        model = Intern
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'date_joined', 
                 'mentor', 'mentor_details', 'internship_end', 'address', 'address_details']
    
    def get_mentor_details(self, obj):
        if obj.mentor:
            return {
                'id': obj.mentor.id,
                'name': f"{obj.mentor.first_name} {obj.mentor.last_name}",
                'department': obj.mentor.department
            }
        return None

class StaffRoleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    role = serializers.CharField()
    type = serializers.CharField()
    address = AddressSerializer()
    
    def to_representation(self, instance):
        if isinstance(instance, Manager):
            serializer = ManagerSerializer(instance)
        elif isinstance(instance, Intern):
            serializer = InternSerializer(instance)
        else:
            raise Exception('Unexpected type of staff member')
        
        data = serializer.data
        data['role'] = instance.get_role()
        data['type'] = instance.__class__.__name__.lower()
        if instance.address:
            data['address'] = AddressSerializer(instance.address).data
        else:
            data['address'] = None
        return data
