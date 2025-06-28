
from django.urls import path
from .views import (
    ManagerListCreateView,
    ManagerRetrieveUpdateDestroyView,
    InternListCreateView,
    InternRetrieveUpdateDestroyView,
    StaffRolesView
)

urlpatterns = [
    path('managers/', ManagerListCreateView.as_view(), name='manager-list-create'),
    path('managers/<int:pk>/', ManagerRetrieveUpdateDestroyView.as_view(), name='manager-retrieve-update-destroy'),
    path('interns/', InternListCreateView.as_view(), name='intern-list-create'),
    path('interns/<int:pk>/', InternRetrieveUpdateDestroyView.as_view(), name='intern-retrieve-update-destroy'),
    path('staff-roles/', StaffRolesView.as_view(), name='staff-roles'),
]