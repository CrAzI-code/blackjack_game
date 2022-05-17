from django.contrib import admin
from .models import PaymentToken, PersonalData

# Register your models here.
admin.site.register(PaymentToken)
admin.site.register(PersonalData)