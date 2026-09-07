from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import BusinessOwner, Bot
from mothers.serializers import BusinessOwnerSerializer, BotSerializer



class GetOneOwnerView(APIView):
    def get(self, request, owner_id):
        try:
            owner = BusinessOwner.objects.get(telegram_id=owner_id)
            serializer = BusinessOwnerSerializer(owner)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"owner not found"},status=status.HTTP_404_NOT_FOUND)


class VerifyOwnerView(APIView):
    def post(self, request):
        if BusinessOwner.objects.filter(telegram_id=request.data["telegram_id"]).exists():
            return Response({"detail":"owner already exists"},status=status.HTTP_400_BAD_REQUEST)
        serializer = BusinessOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)


class GetAllBotOwnerView(APIView):
    def get(self, request, owner_id):
        bots = Bot.objects.filter(owner=owner_id)
        if bots:
            serializer = BotSerializer(bots,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"error":"bots not found"},status=status.HTTP_404_NOT_FOUND)


class GetAllActiveBotOwnerView(APIView):
    def get(self, request, owner_id):
        actives_bot = Bot.objects.filter(status=True,owner=owner_id)
        if actives_bot:
            actives_bot = Bot.objects.filter(status=True,owner=owner_id)
            serializer = BotSerializer(actives_bot,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"error":"when give active bots give a error"},status=status.HTTP_400_BAD_REQUEST)


class GetAllInactiveBotOwnerView(APIView):
    def get(self, request, owner_id):
        actives_bot = Bot.objects.filter(status=False,owner=owner_id)
        if actives_bot:
            actives_bot = Bot.objects.filter(status=False,owner=owner_id)
            serializer = BotSerializer(actives_bot,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"error":"when give inactive bots give a error"},status=status.HTTP_400_BAD_REQUEST)


class CreateBotOwnerView(APIView):
    def post(self, request):
        if Bot.objects.filter(bot_id=request.data["bot_id"]).exists():
            return Response({"detail":"bot already exists"},status=status.HTTP_400_BAD_REQUEST)
        serializer = BotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)


class UpdateBotOwnerView(APIView):
    def put(self, request):
        if not Bot.objects.filter(bot_id=request.data["bot_id"]).filter(owner=request.data["owner"]).exists():
            return Response({"detail":"bot not exists"},status=status.HTTP_404_NOT_FOUND)
        serializer = BotSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)


class DeleteBotOwnerView(APIView):
    def delete(self, request):
        bot = Bot.objects.filter(bot_id=request.data["bot_id"],owner=request.data["owner"])
        if bot:
            bot = Bot.objects.filter(bot_id=request.data["bot_id"],owner=request.data["owner"])
            bot.delete()
            return Response({"detail":"bot deleted"},status=status.HTTP_204_NO_CONTENT)
        return Response({"error":"give error when delete bot"},status=status.HTTP_400_BAD_REQUEST)