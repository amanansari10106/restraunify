from django.urls import path
from baseapp import views

urlpatterns = [
    path('', views.renderWebsiteView, name="renderWebsiteView"),
    path("api/gallery/getfiles/",views.galleryAPI.as_view(), name="galleryAPI" ),
    path("test/", views.test, name="testView")
]