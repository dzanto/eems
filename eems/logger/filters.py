import django_filters
from .models import Claim, Task, Elevator, Address
from django.db.models import Q
# from django.contrib.auth import get_user_model
#
# User = get_user_model()


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
            'address'
        ]

    def claim_and_report_filter(self, queryset, name, value):
        value_list = value.split(' ')
        qs = Claim.objects.none()
        for value in value_list:
            qs = qs | Claim.objects.filter(
                Q(claim_text__icontains=value) |
                Q(report_text__icontains=value)
            )
        return qs

    def address_filter(self, queryset, name, value):
        value_list = value.split(' ')
        qs = Claim.objects.all()
        for value in value_list:
            qs = qs.exclude(
                ~Q(address__street__icontains=value) &
                ~Q(address__house__icontains=value) &
                ~Q(address__entrance__icontains=value)
            )
        return qs


class TaskFilter(django_filters.FilterSet):
    task = django_filters.CharFilter(
        method='task_and_report_filter',
        label='Поиск по планам'
    )
    elevator = django_filters.CharFilter(
        method='elevator_filter',
        label='Адрес'
    )
    # worker = django_filters.ModelChoiceFilter(
    #     queryset=User.objects.all(),
    #     label='Исполнитель'
    # )

    class Meta:
        model = Task
        fields = [
            'task',
            'elevator',
            'worker',
            'fixed',
        ]

    def task_and_report_filter(self, queryset, name, value):
        value_list = value.split(' ')
        qs = Task.objects.none()
        for value in value_list:
            qs = qs | Task.objects.filter(
                Q(task_text__icontains=value) |
                Q(report_text__icontains=value)
            )
        return qs

    def elevator_filter(self, queryset, name, value):
        value_list = value.split(' ')
        qs = Task.objects.all()
        for value in value_list:
            qs = qs.exclude(
                ~Q(elevator__address__street__icontains=value) &
                ~Q(elevator__address__house__icontains=value) &
                ~Q(elevator__address__entrance__icontains=value)
            )
        return qs


class ElevatorFilter(django_filters.FilterSet):

    class Meta:
        model = Elevator
        fields = [
            'address'
        ]