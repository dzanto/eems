import django_filters
from .models import Claim, Task
from django.db.models import Q
from django.db.models import QuerySet


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
        value_list = value.split(' ')
        qs = Claim.objects.filter(claim_text__icontains=value)
        for value in value_list:
            qs = qs | Claim.objects.filter(Q(claim_text__icontains=value) | Q(report_text__icontains=value))
        return qs


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['task_text', 'pub_date', 'elevator', 'worker', 'fix_date', 'report_text']

