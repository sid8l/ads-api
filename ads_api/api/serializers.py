from rest_framework import serializers

from .models import Ad, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("url",)


class AdSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, required=False)
    main_photo = serializers.SerializerMethodField(source="get_main_photo")

    class Meta:
        model = Ad
        fields = ("title", "description", "price", "photos", "main_photo")

    def get_main_photo(self, ad):
        main_photo = Photo.objects.filter(ad=ad).first()
        if main_photo is None:
            return None
        else:
            return main_photo.url

    def create(self, validated_data):
        photos_data = validated_data.pop("photos", [])
        ad = Ad.objects.create(**validated_data)
        photos_objects = [Photo(ad=ad, url=photo.get("url")) for photo in photos_data]
        Photo.objects.bulk_create(photos_objects)
        return ad

    def validate_photos(self, photos):
        if len(photos) > 3:
            raise serializers.ValidationError("Maximum 3 photo")

        urls = [photo.get("url") for photo in photos]
        if len(set(urls)) != len(urls):
            raise serializers.ValidationError("urls per ad must be unique")

        return photos

    def __init__(self, *args, **kwargs):
        context = kwargs.get("context", None)
        fields = None
        if context:
            fields = context.get("fields")

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
