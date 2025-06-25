from django.urls import path
from .views import ChatView

urlpatterns = [

    path(
        'personal_chat/', 
        ChatView.as_view(),  
        name = 'chat'  
    )
]