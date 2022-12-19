from django.urls import path

from api_services import views

urlpatterns = [
    #! Cambiar y preguntar acerca de rutas
    path("api/get", views.Get_Services.as_view(), name='get_services'),
    path("api/post", views.post_services.as_view(), name='get_services'),
    # path("api/pm_app/<int:id>", views.pm_view.as_view(), name='pm_name'),
]