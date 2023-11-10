from django.urls import path
from usersapp import views

urlpatterns = [
    path('signup/', views.signupView, name="signupView"),
    path('login/', views.loginView, name='loginView'),
    path('logout/', views.logoutView, name='logoutView'),
    path("verify/email/<str:token>/", views.verifyEmail, name="verifyEmail"),
    path("forgot-password/", views.forgotPassword, name="forgotPassword"),
    path("forgot-password/email/<str:token>/", views.forgotPasswordEmail, name="forgotPasswordEmail"),
    path("dashboard/", views.dashboardView, name="dashboardView"),
    
    path("api/getdomain/", views.GetDomainAPIView.as_view(), name="getDomainAPI"),
    path("api/deletedomain/", views.DeleteDomainAPIView.as_view(), name="deleteDomainAPI"),
]