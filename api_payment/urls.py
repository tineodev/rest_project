from django.urls import path
from . import views



urlpatterns = [
    path("", views.Get_Payments.as_view(), name='pm_name'),
    # path("<int:id>/", views.pm_view.as_view(), name='pm_name'),
]