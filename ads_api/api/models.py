from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    url = models.CharField(max_length=300)
    upload_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.url
