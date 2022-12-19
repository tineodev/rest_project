from django.urls import path

from api_services import views

urlpatterns = [
    path("api/", views.Get_Services.as_view(), name='get_services'),
    path("api/<int:id>/", views.Rest_services.as_view(), name='rest_services'),
]