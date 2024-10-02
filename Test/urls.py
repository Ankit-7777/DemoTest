from django.urls import path, include
from .views import  UserRegisterAPIView, UserLoginAPIView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='api_register'),
    path('login/', UserLoginAPIView.as_view(), name='api_login'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
