from django.contrib import admin

# Register your models here.
from .models import Address, Claim


class ClaimAdmin(admin.ModelAdmin):
    fields = ['address', 'pub_date', 'claim_text']
    list_display = ('address', 'pub_date', 'claim_text')
    search_fields = ['claim_text']

admin.site.register(Address)
admin.site.register(Claim, ClaimAdmin)
