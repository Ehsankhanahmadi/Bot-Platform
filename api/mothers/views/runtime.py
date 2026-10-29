from django.db.models import F

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import RunTime
from core.permissions import IsMotherRuntime
from mothers.serializers import RunTimeMotherRSerializer



class GetAllRunTimeView(APIView):
    permission_classes = [IsMotherRuntime]
    def get(self, request):
        runtimes = RunTime.objects.filter(runtime_type=RunTime.runtime_type.CHILD,status=True)
        serializer = RunTimeMotherRSerializer(runtimes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class CRUDRunTimeView(APIView):
    permission_classes = [IsMotherRuntime]
    def post(self, request, runtime_id):
        updated = RunTime.objects.filter(runtime_id=runtime_id,status=True).update(bot_count=F("bot_count") + 1)
        if updated == 0:
            return Response({"error": "runtime not found"},status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "bot count runtime incremented"},status=status.HTTP_200_OK)