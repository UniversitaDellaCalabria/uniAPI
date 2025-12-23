from django.conf import settings


ORGANIZATION_API_TOKEN = getattr(settings, 'ORGANIZATION_API_TOKEN', '')
ORGANIZATION_API_GATEWAY = getattr(settings, 'EMPLOYEE_API_GATEWAY', 'https://storage.portale.unical.it/')
ORGANIZATION_API_EMPLOYEE_SERVICE = getattr(settings, 'ORGANIZATION_API_EMPLOYEE_SERVICE', 'api/ricerca/addressbook-full/')
