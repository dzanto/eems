from dal import autocomplete
from . import models
from django.db.models import Q


class AddressAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.Address.objects.all()
        if self.q:
            value_list = self.q.split(' ')
            for value in value_list:
                qs = qs.exclude(
                    ~Q(street__icontains=value) &
                    ~Q(house__icontains=value)
                )
        return qs


class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.User.objects.all()
        if self.q:
            qs = qs.filter(last_name__startswith=self.q)
        return qs


class ElevatorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.Elevator.objects.all()
        if self.q:
            value_list = self.q.split(' ')
            for value in value_list:
                qs = qs.exclude(
                    ~Q(address__street__icontains=value) &
                    ~Q(address__house__icontains=value)
                )
        return qs
