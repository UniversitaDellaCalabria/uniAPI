from drf_spectacular.utils import extend_schema, inline_serializer, OpenApiParameter, OpenApiResponse
from drf_spectacular.types import OpenApiTypes

from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from . serializers import *


class HealthCheckView(APIView):
    """
    Endpoint per il monitoraggio dello stato di salute dell'API (AgID compliant).
    """
    permission_classes = [AllowAny]
    # ~ renderer_classes = [JSONRenderer]
    
    @extend_schema(
        summary="Health check del servizio",
        description="Verifica se l'API è operativa",
        tags=['Monitoraggio'],
        responses={
            200: HealthCheckResponseSerializer
        },
    )
    
    def get(self, request):
        data = {
            "type": f"{request.scheme}://{request.get_host()}/docs#/Monitoraggio/status_retrieve",
            "title": "OK",
            "status": 200,
            "detail": "Il servizio è attivo"
        }
        return Response(data)
