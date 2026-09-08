from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import BusinessOwner, Bot
from mothers.serializers import BusinessOwnerSerializer, BotSerializer



class GetOneOwnerView(APIView):
    def get(self, request, owner_id=None):
        if owner_id is None:
            return Response({"error":"owner_id is required"},status=status.HTTP_400_BAD_REQUEST)
        try:
            owner = BusinessOwner.objects.get(telegram_id=owner_id)
            serializer = BusinessOwnerSerializer(owner)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except BusinessOwner.DoesNotExist as e:
            return Response(e,status=status.HTTP_404_NOT_FOUND)


class VerifyOwnerView(APIView):
    def post(self, request, owner_id=None):
        if owner_id is None or owner_id != request.data["telegram_id"]:
            return Response({"error":"owner_id error please check owner_id is sync with telegram_id in data or check owner_id is not None"},status=status.HTTP_400_BAD_REQUEST)
        if BusinessOwner.objects.filter(telegram_id=owner_id).exists():
            return Response({"detail":"owner already exists"},status=status.HTTP_400_BAD_REQUEST)
        serializer = BusinessOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class GetAllBotOwnerView(APIView):
    def get(self, request, owner_id=None):
        if owner_id is None:
            return Response({"error":"owner_id is required"},status=status.HTTP_400_BAD_REQUEST)
        bots = Bot.objects.filter(owner__telegram_id=owner_id)
        if bots.exists():
            serializer = BotSerializer(bots,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"error":"bots not found"},status=status.HTTP_404_NOT_FOUND)


class GetAllActiveBotOwnerView(APIView):
    def get(self, request, owner_id=None):
        if owner_id is None:
            return Response({"error":"owner_id is required"},status=status.HTTP_400_BAD_REQUEST)
        actives_bot = Bot.objects.filter(status=True,owner__telegram_id=owner_id)
        if actives_bot.exists():
            serializer = BotSerializer(actives_bot,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"error":"when give active bots give a error"},status=status.HTTP_400_BAD_REQUEST)


class GetAllInactiveBotOwnerView(APIView):
    def get(self, request, owner_id=None):
        if owner_id is None:
            return Response({"error":"owner_id is required"},status=status.HTTP_400_BAD_REQUEST)
        inactives_bot = Bot.objects.filter(status=False,owner__telegram_id=owner_id)
        if inactives_bot.exists():
            serializer = BotSerializer(inactives_bot,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"error":"when give inactive bots give a error"},status=status.HTTP_400_BAD_REQUEST)


class CRUDBotOwnerView(APIView):
    def get(self, request, owner_id=None, bot_id=None):
        if owner_id is None or bot_id is None:
            return Response({"error":"owner_id and bot_id is required"},status=status.HTTP_400_BAD_REQUEST)
        bot = Bot.objects.filter(bot_id=bot_id, owner__telegram_id=owner_id)
        if bot.exists():
            serializer = BotSerializer(bot)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"detail":"bot not exists"},status=status.HTTP_404_NOT_FOUND)
        

    def post(self, request, owner_id=None, bot_id=None):
        if owner_id is None or bot_id is None:
            return Response({"error":"owner_id and bot_id is required"},status=status.HTTP_400_BAD_REQUEST)
        if Bot.objects.filter(bot_id=bot_id, owner__telegram_id=owner_id).exists():
            return Response({"detail":"bot already exists"},status=status.HTTP_400_BAD_REQUEST)
        serializer = BotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, owner_id=None, bot_id=None):
        if owner_id is None or bot_id is None:
            return Response({"error":"owner_id and bot_id is required"},status=status.HTTP_400_BAD_REQUEST)
        if not Bot.objects.filter(bot_id=bot_id, owner__telegram_id=owner_id).exists():
            return Response({"detail":"bot not exists"},status=status.HTTP_404_NOT_FOUND)
        serializer = BotSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, owner_id=None, bot_id=None):
        if owner_id is None or bot_id is None:
            return Response({"error":"owner_id and bot_id is required"},status=status.HTTP_400_BAD_REQUEST)
        bot = Bot.objects.filter(bot_id=bot_id, owner__telegram_id=owner_id)
        if bot.exists():
            bot.delete()
            return Response({"detail":"bot deleted"},status=status.HTTP_204_NO_CONTENT)
        return Response({"error":"give error when delete bot"},status=status.HTTP_400_BAD_REQUEST)