from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import RunTime, BusinessOwner, Bot



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
    pass


@admin.register(BusinessOwner)
class BusinessOwnerAdmin(BaseAdmin):
    pass


@admin.register(Bot)
class BotAdmin(BaseAdmin):
    pass