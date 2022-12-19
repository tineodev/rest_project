from django.urls import path
from django.contrib.auth.views import LoginView,logout_then_login	
# from .views import pm_Class


urlpatterns = [
    path('accounts/login', LoginView.as_view(), name='login'),
    # path('register/', pm_class.as_view(), name='register'),
    path('logout', logout_then_login, name='logout'),
]
