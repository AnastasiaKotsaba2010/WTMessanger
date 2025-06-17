from django.urls import path
from .views import RegistrationView, CodeVerificationView, LoginUserView, UserLogoutView


urlpatterns = [

    path(
        'register/', 
        RegistrationView.as_view(),  
        name = 'register'  
    ),
  
    path(
        'register/verify/', 
        CodeVerificationView.as_view(),
        name = 'register-verify'
    ),
    
    path(
        'login/',  
        LoginUserView.as_view(),  
        name = 'login'  
    ),
    path(
        'logout/',
        UserLogoutView.as_view(),
        name = "logout"
    ),
]