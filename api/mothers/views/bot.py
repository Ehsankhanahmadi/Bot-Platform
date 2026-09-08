from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Bot
from mothers.serializers import BotSerializer



class GetAllBotView(APIView):
    def get(self, request):
        try:
            bots = Bot.objects.all()
            serializer = BotSerializer(bots,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Bot.DoesNotExist as e:
            return Response(e,status=status.HTTP_400_BAD_REQUEST)


class GetOneBotView(APIView):
    def get(self, request, bot_id=None):
        if bot_id is None:
            return Response({"error":"bot_id is required"},status=status.HTTP_400_BAD_REQUEST)
        try:
            bot = Bot.objects.get(bot_id=bot_id)
            serializer = BotSerializer(bot)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Bot.DoesNotExist as e:
            return Response(e,status=status.HTTP_400_BAD_REQUEST)