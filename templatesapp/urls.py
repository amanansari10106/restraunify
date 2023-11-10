from django.urls import path
from templatesapp import views

urlpatterns = [
    path('test/', views.templateView, name="test"),
    path('test2/', views.testView, name="test2"),
    path('create/<str:templateid>/', views.createTemplateView, name='createTemplate'),
    path('edit/<str:wid>/', views.editTemplateView, name='editTemplate'),
    path('save/', views.SaveTemplateView.as_view(), name='saveTemplateView'),
    path('preview/<str:wid>/', views.previewWebsite, name='previewWebsite'),
    path('api/createtemplate', views.CreateTemplateAPI.as_view(), name='createWebsiteAPI'),
    path('api/updatedomain', views.UpdateDomainAPI.as_view(), name='updateDomainAPI'),
    path('api/deletewebsite', views.WebsiteDeleteAPI.as_view(), name='deleteWebsiteAPI'),
    
]