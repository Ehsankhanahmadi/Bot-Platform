from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Bot
from mothers.serializers import BotSerializer



class GetAllBotView(APIView):
    def get(self, request):
        bots = Bot.objects.all()
        serializer = BotSerializer(bots,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class GetOneBotView(APIView):
    def get(self, request, bot_id):
        try:
            bot = Bot.objects.get(bot_id=bot_id)
            serializer = BotSerializer(bot)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Bot.DoesNotExist:
            return Response({"error":"bot not found"},status=status.HTTP_404_NOT_FOUND)