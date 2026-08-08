from rest_framework.serializers import ModelSerializer
from ..models import Adapter

class AdapterSerializer(ModelSerializer):
    class Meta:
        model = Adapter
        fields = "__all__"