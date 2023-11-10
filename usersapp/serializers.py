
from rest_framework import serializers
from usersapp.models import FileUploadModel
# from customer.models import

class GallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FileUploadModel
        fields = ["f_id","file","highest"]