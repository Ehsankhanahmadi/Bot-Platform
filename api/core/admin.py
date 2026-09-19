from django.http import JsonResponse
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django.urls import path
from .models import RunTime, BusinessOwner, Bot
from .forms import RunTimeAdminForm



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
        return JsonResponse({"detail": "Token hashed successfully"})


@admin.register(BusinessOwner)
class BusinessOwnerAdmin(BaseAdmin):
    pass


@admin.register(Bot)
class BotAdmin(BaseAdmin):
    pass