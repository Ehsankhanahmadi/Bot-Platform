from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.hashers import check_password

from .models import RunTime



class RuntimeAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization = request.headers.get("Authorization")
        runtime_id = request.headers.get("Runtime")
        if not authorization or not runtime_id:
            return None
        try:
            scheme, token = authorization.split(" ", 1)
        except ValueError:
            raise AuthenticationFailed("Invalid Authorization header.")
        if scheme.lower() != "bearer":
            raise AuthenticationFailed("Authorization scheme must be Bearer.")
        if not token:
            raise AuthenticationFailed("Runtime token is required.")
        try:
            runtime = RunTime.objects.get(runtime_id=runtime_id)
        except RunTime.DoesNotExist:
            raise AuthenticationFailed("Invalid runtime credentials.")
        if not runtime.token:
            raise AuthenticationFailed("Runtime has no token.")
        if not check_password(token, runtime.token):
            raise AuthenticationFailed("Invalid runtime credentials.")
        return (runtime, None)



class IsRuntime(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, RunTime)