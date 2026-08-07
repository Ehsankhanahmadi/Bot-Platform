from rest_framework.views import APIView
from ..models import Adapter
from ..serializers import AdapterSerializer
from rest_framework.response import Response
from rest_framework import status

class CrudAdapter(APIView):
    def get(self, req):
        data = Adapter.objects.all()
        serializer = AdapterSerializer(instance=data,many=True)
        return Response(serializer.data)

    def post(self, req):
        print(req.data)
        serializer = AdapterSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"adapter add","data": serializer.data },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)