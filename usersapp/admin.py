from django.contrib import admin
from usersapp.models import cuser, FileUploadModel, domainsModel
# Register your models here.

admin.site.register(cuser)
admin.site.register(FileUploadModel)
admin.site.register(domainsModel)