from django.contrib import admin

from .models import Address, Claim, Elevator, Owner, Task


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    fields = ['address', 'pub_date', 'claim_text']
    list_display = ('address', 'pub_date', 'claim_text')
    search_fields = ['claim_text']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'house', 'entrance')
    search_fields = ['street', 'house']


@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ('address', 'note')
    search_fields = ['address__street', 'address__house', 'note']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ['elevator', 'pub_date', 'task_text']
    list_display = ('elevator', 'pub_date', 'task_text')
    search_fields = ['elevator__address__street', 'elevator__address__house', 'task_text']


admin.site.register(Owner)
