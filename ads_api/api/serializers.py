from rest_framework import serializers

from .models import Ad, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("url",)


class AdSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Ad
        fields = ("title", "description", "price", "photos")

    def create(self, validated_data):
        photos_data = validated_data.pop("photos")
        ad = Ad.objects.create(**validated_data)
        photos_objects = [Photo(ad=ad, url=photo["url"]) for photo in photos_data]
        Photo.objects.bulk_create(photos_objects)
        return ad


# class AdSerializer(serializers.ModelSerializer):
#     main_photo = serializers.SerializerMethodField("get_main_photo")

#     class Meta:
#         model = Ad
#         fields = ("title", "price", "main_photo")

#     def get_main_photo(self, ad):
#         photo = Photo.objects.filter(ad=ad).first()
#         if photo:
#             return photo.url
#         else:
#             return 0
