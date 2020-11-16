import django_filters
from .models import Claim


class ClaimFilter(django_filters.FilterSet):
    claim_text = django_filters.CharFilter(lookup_expr='icontains')
    address__street = django_filters.CharFilter(lookup_expr='icontains')
    address__house = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Claim
        fields = ['claim_text', 'pub_date']