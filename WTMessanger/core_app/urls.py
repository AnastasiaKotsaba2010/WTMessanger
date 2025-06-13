from django.urls import path
from .views import CoreView, ProfileView


urlpatterns = [
    path('', CoreView.as_view(), name='core'),
    path('details/', ProfileView.as_view(), name= 'details')
]
