import requests

from django.conf import settings
from django.core.cache import cache

from drf_spectacular.utils import extend_schema

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema, inline_serializer, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from uni_esse3api.carriere_service_v1.views import CarriereAPIViewSet

from . serializers import *
from . settings import *

        
@extend_schema(
    tags=['Utilità'],
    parameters=[CheckUserStatusRequestSerializer],
    responses={
        200: CheckUserStatusResponseSerializer
    },
    description="Verifica che status di dipendente e di studente della persona sia regolarmente attivo",
)
class CheckUserStatusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CheckUserStatusRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        cf = serializer.validated_data['cf']

        cache_key = f'v1_checkuserstatus_{cf.lower()}'
        cached_result = cache.get(cache_key)
        if cached_result:
            return Response(cached_result)
            
        result = {'employee': False, 'student': False}
        
        # START check employee
        url = f"{ORGANIZATION_API_GATEWAY}{ORGANIZATION_API_EMPLOYEE_SERVICE}{cf.upper()}/"
        headers = {'Authorization': f'Token {ORGANIZATION_API_TOKEN}'}
        es = requests.get(url, headers=headers)
        if es.status_code == 200:
            result['employee'] = True
        # END check employee
        
        # START check student
        viewset = CarriereAPIViewSet()
        viewset.request = request
        response = viewset.getCarriere(request)
        if response.status_code == 200:
            careers = response.data
            for career in careers:
                if career['staStuCod'] == 'A':
                    result['student'] = True
                    break
        # END check student

        cache.set(cache_key, result)
        return Response(result)
