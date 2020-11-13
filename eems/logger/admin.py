from django.contrib import admin

# Register your models here.
from .models import Address, Claim

admin.site.register(Address)
admin.site.register(Claim)
