from django.shortcuts import render
from templatesapp.models import userWebsites
from usersapp.models import domainsModel
from rest_framework.views import APIView
from baseapp.models import galleryModel
from baseapp.serializers import GallerySerializer
from rest_framework.response import Response

# Create your views here.
from baseapp import utils

def test(request):
    return render(request,"baseapp/test.html")
def renderWebsiteView(request):
    if (not utils.subDomainForWebsiteRender(request.META['HTTP_HOST'])):
        return render(request, "main/index.html", {
            'text':"main website"
        })
    a = domainsModel.objects.get(domain=utils.subDomainForWebsiteRender(request.META['HTTP_HOST'])[0])
    # a = domainsModel.objects.get(domain='google')

    # print(utils.subDomainForWebsiteRender(request.META['HTTP_HOST'][0]))
    b = userWebsites.objects.get(domain=a)
    return render(request, "templatesapp/render.html", {
        'text':b.website_code,
        'headz':b.template.head
    })

class galleryAPI(APIView):

    
    def post(self, request):
        print(request)
        f = galleryModel(user=request.user, type="image", file=request.FILES["file"])
        f.save()
        return Response({"sd":"asd"})

    def get(self, request):
        f = reversed(galleryModel.objects.filter(user=request.user))
        s = GallerySerializer(f, many=True)
        print(s.data)
        return Response(s.data)