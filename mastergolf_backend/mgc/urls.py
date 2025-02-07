from django.contrib import admin
from django.urls import path, include
from apis.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView
from .views import test_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('test/', test_view, name='test'),
    path('admin/', admin.site.urls),
    path('apis/', include('apis.urls')),
    path('apis/login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('apis/logout/', UserViewSet.as_view({'post': 'logout'}), name='logout'),
    path('apis/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apis/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Separate static/media patterns
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)