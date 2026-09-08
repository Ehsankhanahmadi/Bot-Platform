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
        except BusinessOwner.DoesNotExist:
            return Response({"error":"owner not found"},status=status.HTTP_404_NOT_FOUND)


class VerifyOwnerView(APIView):
    def post(self, request, owner_id):
        if owner_id != request.data["telegram_id"]:
            return Response({"error":"owner_id error please check owner_id is sync with telegram_id"},status=status.HTTP_400_BAD_REQUEST)
        if BusinessOwner.objects.filter(telegram_id=owner_id).exists():
            return Response({"detail":"owner already exists"},status=status.HTTP_400_BAD_REQUEST)
        serializer = BusinessOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class GetAllBotOwnerView(APIView):
    def get(self, request, owner_id):
        bots = Bot.objects.filter(owner=owner_id)
        if bots is None:
            return Response({"error":"bots not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = BotSerializer(bots,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class GetAllActiveBotOwnerView(APIView):
    def get(self, request, owner_id):
        actives_bot = Bot.objects.filter(status=True,owner=owner_id)
        if actives_bot is None:
            return Response({"error":"active bots not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = BotSerializer(actives_bot,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class GetAllInactiveBotOwnerView(APIView):
    def get(self, request, owner_id):
        inactives_bot = Bot.objects.filter(status=False,owner=owner_id)
        if inactives_bot is None:
            return Response({"error":"inactive bots not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = BotSerializer(inactives_bot,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class CRUDBotOwnerView(APIView):
    def check_sync(self,request,owner_id,bot_id):
        if request.data["owner"] == owner_id and request.data["bot_id"] == bot_id:
            return True
        return False


    def get(self, request, owner_id, bot_id):
        try:
            bot = Bot.objects.get(bot_id=bot_id, owner=owner_id)
            serializer = BotSerializer(bot)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Bot.DoesNotExist:
            return Response({"error":"bot not exists"},status=status.HTTP_404_NOT_FOUND)


    def post(self, request, owner_id, bot_id):
        check = self.check_sync(request,owner_id,bot_id)
        if not check:
            return Response({"error":"please set true value owner_id and bot_id"})    
        if Bot.objects.filter(bot_id=bot_id).exists():
            return Response({"detail":"bot already exists"},status=status.HTTP_400_BAD_REQUEST)
        serializer = BotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, owner_id, bot_id):
        try:
            bot = Bot.objects.get(bot_id=bot_id, owner=owner_id)  
            serializer = BotSerializer(instance=bot,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Bot.DoesNotExist:
            return Response({"error":"bot not exists"},status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, owner_id, bot_id):
        try:
            bot = Bot.objects.get(bot_id=bot_id, owner=owner_id)
            bot.delete()
            return Response({"detail":"bot deleted"},status=status.HTTP_200_OK)
        except Bot.DoesNotExist:
            return Response({"error":"bot not found"},status=status.HTTP_404_NOT_FOUND)