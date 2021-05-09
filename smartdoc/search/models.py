from django.db import models

# Create your models here.


class Image(models.Model):
    title= models.CharField("title", max_length=100, blank=True, default="title")
    image_file = models.ImageField("image_file", upload_to="uploads/images")
    text = models.TextField("text", blank=True, default="")

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta:
        db_table = "image"


class Audio(models.Model):
    title= models.CharField("title", max_length=100, blank=True, default="title")
    audio_file = models.FileField("audio_file", upload_to="uploads/audio")
    text = models.TextField("text", blank=True, default="")

    def __str__(self):
        return f"{self.pk} {self.title}"

    class Meta:
        db_table = "audio"