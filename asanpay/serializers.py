from rest_framework import serializers
from .models import BannedIP

class BannedIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannedIP
        fields = '__all__'