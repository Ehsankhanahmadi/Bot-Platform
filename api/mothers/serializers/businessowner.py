from rest_framework import serializers
from core.models import BusinessOwner



class BusinessOwnerRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessOwner
        fields = "__all__"
        read_only_fields = ["user_name","telegram_id","phone_number"]


    def validate(self, attrs):
        return super().validate(attrs)



class BusinessOwnerVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessOwner
        fields = "__all__"


    def validate(self, attrs):
        return super().validate(attrs)