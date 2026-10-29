from rest_framework import serializers
from core.models import Bot



class BotRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = "__all__"
        read_only_fields = ['bot_username','bot_id','owner','assignment']

    def validate(self, attrs):
        return super().validate(attrs)



class BotCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = "__all__"


    def validate(self, attrs):
        return super().validate(attrs)