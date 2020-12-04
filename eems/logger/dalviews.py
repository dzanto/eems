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
