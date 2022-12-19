from django.shortcuts import render, redirect

from .forms import ApiRegister
from django.views.generic import CreateView

# Create your views here.

class SignupCreateView(CreateView):
    form_class = ApiRegister
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return redirect('login')
