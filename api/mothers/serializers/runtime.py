from rest_framework import serializers
from core.models import RunTime



class RunTimeMotherRSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunTime
        fields = ["runtime_id","status","bot_count"]
        read_only_fields = ["runtime_id","status","bot_count"]


    def validate(self, attrs):
        return super().validate(attrs)



class RunTimeBackendRUSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunTime
        fields = ["runtime_id","url","status","bot_count"]
        read_only_fields = ["runtime_id","url","status","bot_count"]


    def validate(self, attrs):
        return super().validate(attrs)