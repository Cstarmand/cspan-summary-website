from .models import CSPANdata
from rest_framework import serializers

class CSPANSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSPANdata
        fields = ['id','name','description']