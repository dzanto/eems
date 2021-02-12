from django.contrib import admin

# Register your models here.
from .models import Address, Claim, Elevator, Owner, Task


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    fields = ['address', 'pub_date', 'claim_text']
    list_display = ('address', 'pub_date', 'claim_text')
    search_fields = ['claim_text']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'house', 'entrance')
    search_fields = ['street', 'house',]

admin.site.register(Elevator)
admin.site.register(Owner)
admin.site.register(Task)
