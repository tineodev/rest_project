from django.urls import path

from api_services import views

urlpatterns = [
    path("api/", views.Get_Services.as_view(), name='get_services'),
    # path("api/pm_app/<int:id>", views.pm_view.as_view(), name='pm_name'),
]