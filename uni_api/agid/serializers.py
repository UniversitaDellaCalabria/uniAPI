from rest_framework import serializers

  
class HealthCheckResponseSerializer(serializers.Serializer):
    type = serializers.URLField()
    title = serializers.CharField()
    status = serializers.IntegerField()
    detail = serializers.CharField()
