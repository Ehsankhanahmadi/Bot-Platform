from rest_framework import serializers
from core.models import RunTime



class RunTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunTime
        fields = "__all__"


    def validate(self, attrs):
        return super().validate(attrs)