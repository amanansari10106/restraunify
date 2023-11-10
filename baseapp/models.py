from django.db import models
from django.contrib.auth.models import User
import os
from restraunify import settings
# Create your models here.

fileTypes = (
    ("image", "IMAGE"),
    ("video", "VIDEO")
)


class galleryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=fileTypes)
    file = models.FileField(upload_to='files/', default='')

    def delete(self, *args, **kwargs):
        fpath = str(settings.BASE_DIR) + "/" + "filesdir" + "/" + str(self.file)
        if os.path.exists(fpath):
            os.remove(fpath)
        super().delete(*args, **kwargs)

