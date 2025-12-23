from rest_framework import serializers


class CheckUserStatusRequestSerializer(serializers.Serializer):
    cf = serializers.CharField(
        required=True, 
        min_length=16, 
        max_length=16,
        help_text="Il codice fiscale dello studente"
    )

    
class CheckUserStatusResponseSerializer(serializers.Serializer):
    employee = serializers.BooleanField()
    student = serializers.BooleanField()
