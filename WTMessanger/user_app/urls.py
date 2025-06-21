from django.urls import path
from .views import RegistrationView, LoginUserView, UserLogoutView, MainFriendsView, AllFriendsView, RecommendedFriendsView, FriendshipRequestView, PersonalInformationView


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
  
    path(
        'logout/',
        UserLogoutView.as_view(),
        name = "logout"
    ),
    # path(
    #     'register/verify/', 
    #     CodeVerificationView.as_view(),
    #     name = 'register-verify'
    # ),
    
    path(
        'friends/main/', 
        MainFriendsView.as_view(), 
        name = 'main_friends'
    ),
    path(
        'friends/all/', 
        AllFriendsView.as_view(), 
        name = 'all_friends'
    ),
    path(
        'friends/recommended/', 
        RecommendedFriendsView.as_view(), 
        name = 'recommended_friends'
    ),
    path(
        'friends/requests/', 
        FriendshipRequestView.as_view(), 
        name = 'friendship_requests'
    ),
    
    # 
    path(
        'settings/',
        PersonalInformationView.as_view(), 
        name = 'personal_information'
    )
    
]