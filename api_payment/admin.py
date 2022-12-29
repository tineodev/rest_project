from django.contrib import admin

# Register your models here.
from .models import Payments, Payments_expired

admin.site.register(Payments)
admin.site.register(Payments_expired)