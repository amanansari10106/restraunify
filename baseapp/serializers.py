from rest_framework import serializers
from baseapp.models import galleryModel

class GallerySerializer(serializers.ModelSerializer):

    url_length = serializers.SerializerMethodField('_get_highest_price')

    def _get_highest_price(self, driver_object):
        # global highest
        lenz = len(str(getattr(driver_object, "file")))
        # if highest_price and highest_price<price:
        #     highest = price
        #     return highest
        # highest = 20
        return lenz


    class Meta:
        model = galleryModel
        fields = ["file","url_length"]