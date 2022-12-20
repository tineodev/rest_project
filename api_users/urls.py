from django.urls import path
from django.contrib.auth.views import LoginView,logout_then_login	
from .views import SignupCreateView, Index, login_view


urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('register/', SignupCreateView.as_view(), name='register'),
    path('logout/', logout_then_login, name='logout'),
    path('index/', Index.as_view(), name='index'),
]
