from django.urls import path
from .views import CrudAdapter

urlpatterns = [
    path("adapters/", CrudAdapter.as_view(), name="crud_adapter"),
]