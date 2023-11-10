from django.shortcuts import render
from django.contrib.auth.models import User
from usersapp.models import cuser
from usersapp import usersAppUtils
import uuid
from django.http import HttpResponse
from restraunify import settings
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from usersapp.models  import ResetPasswordModel
from django.db.models import Q
import threading
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from usersapp.models import FileUploadModel
from usersapp.serializers import GallerySerializer
from templatesapp.models import templatesModel, userWebsites
from usersapp.models import domainsModel
from restraunify import settings
# Create your views here.

def logoutView(request):
    logout( request)
    return HttpResponseRedirect(reverse('loginView'))


def loginView(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        password = request.POST["pass"]
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            if cuser.objects.get(user=user).is_verified:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboardView'))
                
            return render(request, "usersapp/signup_ack.html")
            
        else:
            return render(request, "usersapp/login.html", {
                "message": "Invalid username and/or password."
        })


    return render(request,"usersapp/login.html")


def signupView(request):
    if request.method == "GET":
        return render(request, "usersapp/signup.html")
    
    fName = request.POST["fname"]
    lName = request.POST["lname"]
    uName = request.POST["uname"]
    if(User.objects.filter(username=uName).exists()):
        return render(request, "usersapp/signup.html",{
            "unameError":"Username not available"
        })
    
    phoneNo = request.POST["phoneNo"]
    password = request.POST["pass"]
    email = request.POST["email"]
    if(cuser.objects.filter(email=email, is_verified=True).exists()):

        return render(request, "usersapp/signup.html",{
            "emailError":"Email not available"
        })
    user = User.objects.create_user(uName, email, password)
    user.save()
    tuser = cuser(user=user, username=uName, email=email, fName=fName, lName= lName, phoneNo=phoneNo, utoken=str(uuid.uuid4()))
    tuser.save()
    subject = "welcome to Restraunify Bank"
    message = f'Hi {fName}. \n thank you for registering in restraunify. \n click on this link : {settings.HOST_URL}user/verify/email/{tuser.utoken}/ to verify your account \n Username : {user.username}'
    t = threading.Thread(target=usersAppUtils.sendmail, args=(email, message, subject))
    # usersAppUtils.sendmail(email, message, subject)
    t.start()
    return render(request, "usersapp/signup_ack.html")

def verifyEmail(request,token):
    if cuser.objects.filter(utoken=token).exists():
        f = cuser.objects.get(utoken=token)
        f.is_verified = True
        f.save()
        z = User.objects.filter(email=f.email).exclude(username=f.username)
        if z.exists():
            for a in z:
                a.delete()
        login(request, f.user)
        # return HttpResponse("signed in as")
        return HttpResponseRedirect(reverse("dashboardView"))
    else:
        return HttpResponse("no uuid exist")

def forgotPassword(request):
    if request.method == "POST":
        term = request.POST["email/username"]
        tuser = User.objects.get(Q(email=term)|Q(username=term))
        if ResetPasswordModel.objects.filter(user=tuser).exists():
            obj = ResetPasswordModel.objects.get(user=tuser)
            obj.delete()
        # tuser = User.objects.get(username=term) | User.objects.get(email=term)
        if not tuser:
            return render(request, "usersapp/forgotPassword.html",{
                "error":"No account is present with this email / username"
            })
        
        token = str(uuid.uuid4())
        obj = ResetPasswordModel(user=tuser, token=token)
        obj.save()
        message = f'To reset your password click on this link : {settings.HOST_URL}user/forgot-password/email/{obj.token}/'
        subject = "Reset Password By PLF"
        email = tuser.email
        usersAppUtils.sendmail(email, message,subject)
        return render(request,"usersapp/forgotPassword_ack.html")
    
    return render(request,"usersapp/forgotPassword.html")

def forgotPasswordEmail(request, token):
    if request.method == "POST":
        password = request.POST["password"]
        tuser = request.user
        tuser.set_password(password)
        tuser.save()
        obj = ResetPasswordModel.objects.get(user=request.user)
        obj.delete()
        return HttpResponseRedirect(reverse("loginView"))
    if not ResetPasswordModel.objects.filter(token=token).exists():
        return HttpResponse("link expired generate new link")
    obj = ResetPasswordModel.objects.get(token=token)
    login(request, obj.user)
    return render(request,"usersapp/enterResetPassword.html")


def dashboardView(request):
    host = request.META["HTTP_HOST"]
    # return render(request,"restrauntTemplates/test.html" , {"host":host})
    templates = templatesModel.objects.all()
    websites =  userWebsites.objects.filter(user=request.user.cuser)
    domains = domainsModel.objects.filter(user=request.user)
    return render(request,"usersapp/dashboard.html", {
        'templates':templates,
        'websites': websites,
        'active':'templates',
        'domains':domains,
        'settings':settings
    })


class GalleryAPI(APIView):
    def get(self, request):
        f = FileUploadModel.objects.filter(user=request.user)
        ser = GallerySerializer(f, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    
class GetDomainAPIView(APIView):

    def post(self, request):
        domain = request.data["domain"]
        if domainsModel.objects.filter(domain=domain).exists():
            return Response({"resp":"fail"}, status=status.HTTP_400_BAD_REQUEST)
        a = domainsModel(domain=domain, user=request.user)
        a.save()
        return Response({"resp":"success"}, status=status.HTTP_200_OK)
    
class DeleteDomainAPIView(APIView):

    def delete(self, request):
        did = request.data["did"]
        if domainsModel.objects.filter(id=did, user=request.user).exists():
            domainsModel.objects.get(id=did, user=request.user).delete()
            return Response({"resp":"success"}, status=status.HTTP_200_OK)
        return Response({"resp":"fail"}, status=status.HTTP_400_BAD_REQUEST)