# Create your tests here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DataEngCsv
from .serializers import TestDataSerializer

@api_view(['GET'])


def getTestDatas(request):
    datas = DataEngCsv.objects.filter(daiso = 1)
    serializer = TestDataSerializer(datas, many=True)
    return Response(print(serializer.data))