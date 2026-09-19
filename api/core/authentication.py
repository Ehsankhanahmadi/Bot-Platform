from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from .models import RunTime
from django.contrib.auth.hashers import check_password



class RuntimeAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token_auth_header = request.headers.get("Authorization")
        runtime_id_header = request.headers.get("Runtime")
        if not token_auth_header or not runtime_id_header :
            return None
        try:
            scheme, token = token_auth_header.split(" ", 1)
        except ValueError:
            raise AuthenticationFailed("Invalid Authorization header.")
        if scheme.lower() != "bearer":
            raise AuthenticationFailed("Authorization scheme must be Bearer.")
        try:
            runtime = RunTime.objects.get(runtime_id=runtime_id_header)
            if runtime.token and check_password(runtime.token):
                return (runtime, None)
        except Exception as e :
            print(e)
            raise AuthenticationFailed("Invalid runtime token.")



class IsRuntime(BasePermission):
    def has_permission(self, request, view):
        return request.auth is not None