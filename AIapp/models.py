from django.db import models

# Create your models here.


class Imageai(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default="")
    image_ai = models.ImageField(upload_to="mediaai", blank = True, null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        varbose_name = "Imageia"
        varbose_name_plural = "Obrazy AI"