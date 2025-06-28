from rest_framework import serializers
from .models import Manager, Intern

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'date_joined', 'department']
        read_only_fields = ['has_company_card']

class InternSerializer(serializers.ModelSerializer):
    mentor_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Intern
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'date_joined', 
                 'mentor', 'mentor_details', 'internship_end']
    
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
        return data

