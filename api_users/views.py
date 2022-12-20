from django.shortcuts import render, redirect

from .forms import ApiRegister
from django.views.generic import CreateView, View

from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class SignupCreateView(CreateView):
    form_class = ApiRegister
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return redirect('login')


class Index(LoginRequiredMixin,View):
    def get(self, request):
        template_name = 'api_users/index.html'
        return render(request, template_name)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            refresh_token = RefreshToken.for_user(request.user)
            token = str(refresh_token)
            context = {'token': token}
            return render(request, 'api_users/index.html', context)
        else:
            error_message = 'Usuario o contraseña inválidos'
            context = {'error_message': error_message}
            return render(request, 'registration/login.html', context)
    else:
        return render(request, 'registration/login.html')