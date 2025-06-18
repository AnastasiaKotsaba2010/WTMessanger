from django.urls import path
from .views import RegistrationView, LoginUserView


urlpatterns = [

    path(
        'register/', 
        RegistrationView.as_view(),  
        name = 'register'  
    ),
    path(
        'login/',  
        LoginUserView.as_view(),  
        name = 'login'  
    ),
  
    # path(
    #     'register/verify/', 
    #     CodeVerificationView.as_view(),
    #     name = 'register-verify'
    # ),
    
    # path(
    #     'logout/',
    #     UserLogoutView.as_view(),
    #     name = "logout"
    # ),
]