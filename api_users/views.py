from django.shortcuts import render, redirect

from .forms import ApiRegister
from django.views.generic import CreateView, View

from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.mixins import LoginRequiredMixin

from api_services.models import Services


from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view



from django.contrib.auth.models import User
from django.http import JsonResponse

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
            token = str(refresh_token.access_token)
            context = {
                'token': token,
                "services":Services.objects.all()
                }
            return render(request, 'api_users/index.html', context)
        else:
            error_message = 'Usuario o contraseña inválidos'
            context = {'error_message': error_message}
            return render(request, 'registration/login.html', context)
    else:
        return render(request, 'registration/login.html')

@api_view(['GET'])
def get_user(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    return Response({'id': user.id, 'is_staff':user.is_staff, 'username':user.username})



# def register_new(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = User.objects.create_user(username=username, password=password)
#         user.save()

#         return JsonResponse({'status': 'ok'})
#     return JsonResponse({'status': 'error'})
