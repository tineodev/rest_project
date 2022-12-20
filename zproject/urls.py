"""zproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api_payment.views import Rest_Payments, Rest_Payments_expired
from api_services.views import Rest_Services
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView





router = routers.DefaultRouter()
router.register(r'services', Rest_Services, 'Services')
router.register(r'payments', Rest_Payments, 'Payments')
router.register(r'payments-expired', Rest_Payments_expired, 'Payments-expired')


schema_view = get_schema_view(
    openapi.Info(
        title="API Payments",
        default_version='v1',
        description="Proyecto TODO API de Silabuz",
        terms_of_service="https://github.com/tineodev",
        contact=openapi.Contact(email="tineo.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_users.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(),  name="refresh_token"),
]

urlpatterns += router.urls
