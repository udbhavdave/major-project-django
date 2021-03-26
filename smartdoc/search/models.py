from django.db import models

# Create your models here.


class Image(models.Model):
    title= models.CharField(max_length=50, blank=True, default="title")
    image_file = models.ImageField(upload_to="uploads/images")
    text = models.CharField(max_length=5000, blank=True, default="image text")

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta:
        db_table = "image"


class Audio(models.Model):
    title= models.CharField(max_length=50, blank=True, default="title")
    audio_file = models.FileField(upload_to="uploads/audio")
    text = models.CharField(max_length=5000, blank=True, default="audio text")

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta:
        db_table = "audio"
