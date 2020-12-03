import django_filters
from .models import Claim, Task
from django.db.models import Q


class ClaimFilter(django_filters.FilterSet):
    claim = django_filters.CharFilter(
        method='claim_and_report_filter',
        label='Текст заявки'
    )

    address = django_filters.CharFilter(
        method='address_filter',
        label='Адрес'
    )

    class Meta:
        model = Claim
        fields = [
            'claim',
            'pub_date',
            'address'
        ]

    def claim_and_report_filter(self, queryset, name, value):
        value_list = value.split(' ')
        qs = Claim.objects.filter(claim_text__icontains=value)
        for value in value_list:
            qs = qs | Claim.objects.filter(
                Q(claim_text__icontains=value) |
                Q(report_text__icontains=value)
            )
        return qs

    def address_filter(self, queryset, name, value):
        value_list = value.split(' ')
        qs = Claim.objects.filter(
            Q(address__street__icontains=value_list[0]) |
            Q(address__house__icontains=value_list[0]) |
            Q(address__entrance__icontains=value_list[0])
        )
        if len(value_list) == 1:
            return qs
        else:
            for value in value_list:
                qs = qs & Claim.objects.filter(
                    Q(address__street__icontains=value) |
                    Q(address__house__icontains=value) |
                    Q(address__entrance__icontains=value)
                )
            return qs


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['task_text', 'pub_date', 'elevator', 'worker', 'fix_date', 'report_text']

