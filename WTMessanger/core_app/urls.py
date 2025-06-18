from django.urls import path
from .views import CoreView


urlpatterns = [
    path('', CoreView.as_view(), name='core'),
    # path('details/', ProfileView.as_view(), name= 'details'),
    # path('settings/', SettingsView.as_view(), name='settings'),
]
