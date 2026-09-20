from django.http import JsonResponse
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.hashers import make_password
from django.urls import path

from .models import RunTime, BusinessOwner, Bot
from .forms import RunTimeAdminForm
from .cache import delete_runtime_cache


class BaseAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("core/css/custom_admin.css",)
        }



admin.site.unregister(User)
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    class Media:
        css = {
            "all": ("core/css/custom_admin.css",)
        }



@admin.register(RunTime)
class RunTimeAdmin(BaseAdmin):
    form = RunTimeAdminForm
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<path:object_id>/hash-token/",
                self.admin_site.admin_view(self.hash_token),
                name="runtime-hash-token",
            ),
            path(
                "<path:object_id>/clear-cache/",
                self.admin_site.admin_view(self.clear_cache),
                name="runtime-clear-cache",
            ),
            path(
                "<path:object_id>/password-clear-cache/",
                self.admin_site.admin_view(self.password_clear_cache),
                name="runtime-password-clear-cache",
            ),

        ]
        return custom_urls + urls


    def hash_token(self, request, object_id):
        if request.method != "POST":
            return JsonResponse({"error": "POST request required"},status=405)
        runtime = self.get_object(request, object_id)
        if runtime is None:
            return JsonResponse({"error": "Runtime not found"},status=404)
        token = request.POST.get("token")
        if not token:
            return JsonResponse({"error": "Token is required"},status=400)
        hashed_token = make_password(token)
        runtime.token = hashed_token
        runtime.save(update_fields=["token"])
        delete_runtime_cache(runtime.runtime_id)
        return JsonResponse({"detail": "Token hashed successfully"})


    def clear_cache(self, request, object_id):
        if request.method != "POST":
            return JsonResponse({"error": "POST request required"},status=405)
        runtime = self.get_object(request, object_id)
        if runtime is None:
            return JsonResponse({"error": "Runtime not found"},status=404)
        status_value = request.POST.get("status")
        if status_value is None:
            return JsonResponse({"error": "status is required"}, status=400)
        runtime.status = status_value.lower() == "true"
        runtime.save(update_fields=["status"])
        delete_runtime_cache(runtime.runtime_id)
        return JsonResponse({"detail": "Clear cache and change status successfully"})


    def password_clear_cache(self, request, object_id):
        if request.method != "POST":
            return JsonResponse({"error": "POST request required"},status=405)
        runtime = self.get_object(request, object_id)
        if runtime is None:
            return JsonResponse({"error": "Runtime not found"},status=404)
        password_value = request.POST.get("password")
        if password_value is None:
            return JsonResponse({"error": "password value is required"}, status=400)
        runtime.password = password_value
        runtime.save(update_fields=["password"])
        delete_runtime_cache(runtime.runtime_id)
        return JsonResponse({"detail": "Password clear cache successfully"})



@admin.register(BusinessOwner)
class BusinessOwnerAdmin(BaseAdmin):
    pass



@admin.register(Bot)
class BotAdmin(BaseAdmin):
    pass