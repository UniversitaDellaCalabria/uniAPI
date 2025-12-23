import requests

from django.conf import settings

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from uni_esse3api.carriere_service_v1.views import CarriereAPIView

from . settings import *


class CheckUserStatusAPIView(APIView):
    
    name = "CheckUserStatus"
    description = "Controlla lo stato dell'utente e restituisce.... da completare"
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        cf = request.GET.get('cf')
        if not cf:
            return Response(
                status=400,
                data="Parametro GET 'cf' (codice fiscale) mancante"
            )

        result = {'employee': False, 'student': False}

        # START check employee
        url = f"{ORGANIZATION_API_GATEWAY}{ORGANIZATION_API_EMPLOYEE_SERVICE}{cf}/"
        headers = {'Authorization': f'Token {ORGANIZATION_API_TOKEN}'}
        es = requests.get(url, headers=headers)
        if es.status_code == 200:
            result['employee'] = True
        # END check employee
        
        # START check student
        esse3_carriere_service_v1_carriere = CarriereAPIView.as_view(
            action='getCarriere',
            permission_classes=[]
        )
        
        response = esse3_carriere_service_v1_carriere(request._request)
        if response.status_code == 200:
            careers = response.data
            for career in careers:
                if career['staStuCod'] == 'A':
                    result['student'] = True
                    break
        # END check student
        
        return Response(result)
