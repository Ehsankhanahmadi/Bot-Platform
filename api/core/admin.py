from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.urls import path
from django.shortcuts import redirect
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
                "<path:object_id>/generate-token/",
                self.admin_site.admin_view(self.generate_token),
                name="runtime-generate-token",
            ),
        ]
        return custom_urls + urls

    def generate_token(self, request, object_id):
        runtime = self.get_object(request, object_id)
        print("Generate token for:", runtime)
        return redirect("admin:core_runtime_change",object_id)


@admin.register(BusinessOwner)
class BusinessOwnerAdmin(BaseAdmin):
    pass


@admin.register(Bot)
class BotAdmin(BaseAdmin):
    pass