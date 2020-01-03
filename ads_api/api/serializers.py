from rest_framework import serializers

from .models import Ad


class AdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ad
        fields = ("title", "description")
