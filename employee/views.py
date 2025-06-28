from rest_framework import generics, mixins
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer, StaffRoleSerializer

class ManagerListCreateView(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class InternListCreateView(generics.ListCreateAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

class InternRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

class StaffRolesView(generics.ListAPIView):
    def get_queryset(self):
        managers = Manager.objects.all()
        interns = Intern.objects.all()
        return list(managers) + list(interns)
    
    serializer_class = StaffRoleSerializer

