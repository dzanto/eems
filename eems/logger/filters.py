import django_filters
from .models import Claim
from django.db.models import Q


class ClaimFilter(django_filters.FilterSet):
    claim = django_filters.CharFilter(
        method='claim_and_report_filter',
        label='Текст заявки'
    )
    address__street = django_filters.CharFilter(lookup_expr='icontains')
    address__house = django_filters.CharFilter(lookup_expr='icontains')
    address__entrance = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Claim
        fields = ['claim', 'pub_date', 'address__street', 'address__house', 'address__entrance']

    def claim_and_report_filter(self, queryset, name, value):
        return Claim.objects.filter(
            Q(claim_text__icontains=value) | Q(report_text__icontains=value)
        )

