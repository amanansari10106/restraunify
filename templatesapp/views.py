from django.shortcuts import render
from templatesapp.models import userWebsites
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from baseapp import utils as templatesUtils
from templatesapp.models import userWebsites, templatesModel
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from usersapp.models import cuser, domainsModel
from restraunify import settings

def templateView(request):
    text = userWebsites.objects.all().first().website_code
    return render(request,"templatesapp/render.html",{
        'text':text
    } )

def createTemplateView(request, templateid):
    f = templatesModel.objects.get(id=templateid)
    zuser = cuser.objects.get(user=request.user)
    z = userWebsites(user=zuser, website_code=f.code, template=f)
    z.save()
    return HttpResponseRedirect(reverse('editTemplate',kwargs={"wid":z.id}))
    # return HttpResponseRedirect(reverse('previewWebsite',kwargs={"wid":z.id}))
    # return render(request, 'templatesapp/editTemplate.html', {
    #     'code':f.code,
    #     'headz':f.head,
    #     'wid':z.id
    # })

class CreateTemplateAPI(APIView):
    def post(self, request):
        tid = request.data["tid"]
        wname = request.data["wname"]
        f = templatesModel.objects.get(id=tid)
        z = userWebsites(user=request.user.cuser, website_code=f.code, template=f, name=wname)
        z.save()

        return Response({"wid":z.id}, status=status.HTTP_200_OK)



def testView(request):
    return HttpResponseRedirect(reverse('previewWebsite',kwargs={"wid":20}))
def editTemplateView(request, wid):
    f = userWebsites.objects.get(id=wid)
    domains = domainsModel.objects.filter(user=request.user, userwebsites=None)
    return render (request, 'templatesapp/editTemplate.html', {
        'code':f.website_code,
        'headz':f.template.head,
        'wid':f.id,
        'website': f,
        'domains':domains,
        'settings': settings
    })
    
def previewWebsite(request, wid):
    f = userWebsites.objects.get(id=wid)
    
    return render (request, 'templatesapp/previewWebsite.html',{
        'code':f.website_code,
        'headz':f.template.head,
        
    })

class SaveTemplateView(APIView):

    def post(self, request):
        code = request.data["code"]
        wid = request.data["wid"]
        website = userWebsites.objects.get(id=wid)
        website.website_code = code
        website.save()
        msg = {
            'resp':'sucess'
        }
        return Response(msg, status=status.HTTP_200_OK)
        # pass

# def previewView(request, wid):
#     f = userWebsites.objects.get(id=wid)
#     return render()

class UpdateDomainAPI(APIView):

    def post(self, request):
        domain = request.data["domain"]
        wid = request.data["wid"]

        web =  userWebsites.objects.get(id=wid, user=request.user.cuser)
        if domain == "remove":
            web.domain = None
            web.save()
            return Response({"resp":"success"}, status=status.HTTP_200_OK)
        d = domainsModel.objects.get(domain=domain, user=request.user)
        web.domain = d
        web.save()
        return Response({"resp":"success"}, status=status.HTTP_200_OK)

class WebsiteDeleteAPI(APIView):

    def delete(self, request):
        web = userWebsites.objects.get(id=request.data["wid"], user=request.user.cuser)
        web.delete()
        return Response({"resp":"sucess"}, status=status.HTTP_200_OK)