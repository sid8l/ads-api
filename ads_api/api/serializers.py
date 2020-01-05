from rest_framework import serializers

from .models import Ad, Photo


class AdSerializer(serializers.ModelSerializer):
    main_photo = serializers.SerializerMethodField("get_main_photo")

    class Meta:
        model = Ad
        fields = ("title", "price", "main_photo")

    def get_main_photo(self, ad):
        photo = Photo.objects.filter(ad=ad).first()
        if photo:
            return photo.url
        else:
            return 0
