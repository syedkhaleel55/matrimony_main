from rest_framework import serializers
from .models import *

class BasicinformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = '_all_'