from dal import autocomplete
from . import models


class AddressAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.Address.objects.all()
        if self.q:
            qs = qs.filter(street__istartswith=self.q)

        return qs
