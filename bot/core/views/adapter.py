from rest_framework.views import APIView
from ..models import Adapter
from ..serializers import AdapterSerializer
from rest_framework.response import Response

class CrudAdapter(APIView):
    def get(self, req):
        data = Adapter.objects.all()
        serializer = AdapterSerializer(data,many=True)
        return Response(serializer.data)

    def post(self, req):
        pass