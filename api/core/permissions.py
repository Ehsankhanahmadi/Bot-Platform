from rest_framework.permissions import BasePermission

from .models import RunTime



class IsRuntime(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, RunTime)



class IsChildRuntime(BasePermission):
    def has_permission(self, request, view):
        return (isinstance(request.user, RunTime) and request.user.runtime_type == RunTime.RuntimeType.CHILD)



class IsMotherRuntime(BasePermission):
    def has_permission(self, request, view):
        return (isinstance(request.user, RunTime) and request.user.runtime_type == RunTime.RuntimeType.MOTHER)