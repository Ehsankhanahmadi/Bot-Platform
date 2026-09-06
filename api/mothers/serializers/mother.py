from rest_framework import serializers
from core.models import RunTime, BusinessOwner, Bot



class RunTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunTime
        fields = "__all__"


class BusinessOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessOwner
        fields = "__all__"


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = "__all__"