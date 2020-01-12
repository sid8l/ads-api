from rest_framework import viewsets, filters, mixins, status
from rest_framework.response import Response

from .models import Ad
from .serializers import AdSerializer


class AdViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["price", "created_at"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"id": instance.id, "status": status.HTTP_201_CREATED},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def perform_create(self, serializer):
        return serializer.save()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        custom_fields = context["request"].query_params.get("fields")
        action = self.action

        default_read_fields = ["title", "price", "main_photo"]
        default_write_fields = ["title", "description", "price", "photos"]

        if action == "list":
            context["fields"] = default_read_fields
        elif action == "create":
            context["fields"] = default_write_fields
        elif action == "retrieve":
            if custom_fields:
                custom_fields = custom_fields.split(",")
                context["fields"] = default_read_fields + custom_fields
            else:
                context["fields"] = default_read_fields
        return context
