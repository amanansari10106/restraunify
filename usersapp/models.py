from django.db import models
from django.contrib.auth.models import User
from restraunify import settings
import os
# Create your models here.

class cuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    phoneNo = models.IntegerField()
    utoken = models.CharField(max_length=200, default="")
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class ResetPasswordModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.TextField()


class FileUploadModel(models.Model):
    f_id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=50)
    user = models.ForeignKey(cuser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='userUploads/')

    def delete(self, *args, **kwargs):
        fpath = str(settings.BASE_DIR) + "/" + "filesdir" + "/" + str(self.file)
        if os.path.exists(fpath):
            os.remove(fpath)
        super().delete(*args, **kwargs)

class domainsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=200)
    