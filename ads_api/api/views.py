from rest_framework import viewsets, filters

from .models import Ad
from .serializers import AdSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["price", "created_at"]
