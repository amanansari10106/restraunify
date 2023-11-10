from django.db import models
from usersapp.models import cuser
from usersapp.models import domainsModel

# Create your models here.

websiteStatus = (
    ("draft", "DRAFT"),
    ("published", "PUBLISHED")
)

class templatesModel(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.TextField()
    head = models.TextField(default="")
    title = models.CharField(max_length=100, default="")
    image = models.TextField(default="")
class userWebsites(models.Model):
    user = models.ForeignKey(cuser, on_delete=models.CASCADE)
    website_code = models.TextField()
    domain = models.OneToOneField(domainsModel, on_delete=models.SET_NULL, null=True, default="")
    status = models.TextField(choices=websiteStatus, default='draft')
    template = models.ForeignKey(templatesModel, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, default="Website Name")


