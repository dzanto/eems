import django_tables2 as tables
from django_tables2.utils import A
from .models import Claim, Task, Address, Elevator
from .filters import ClaimFilter


class ClaimTable(tables.Table):
    class Meta:
        model = Claim
        template_name = 'includes/bootstrap4.html'
        fields = ['pub_date', 'elevator', 'claim_text', 'fix_date_time', 'report_text', 'worker', 'author']

    claim_text = tables.Column(linkify=("logger:claim_edit", [tables.A("pk")]))
    pub_date = tables.DateTimeColumn(format='d.m.Y G:i')
    fix_date_time = tables.DateColumn(format='d.m.Y G:i')


class OtherClaimTable(tables.Table):
    class Meta:
        model = Claim
        template_name = 'includes/bootstrap4.html'
        fields = ['pub_date', 'address', 'claim_text', 'fix_date_time', 'report_text', 'worker', 'author']

    claim_text = tables.Column(linkify=("logger:other_claim_edit", [tables.A("pk")]))
    pub_date = tables.DateTimeColumn(format='d.m.Y G:i')
    fix_date_time = tables.DateColumn(format='d.m.Y G:i')


class TaskTable(tables.Table):
    class Meta:
        model = Task
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['pub_date', 'elevator', 'task_text', 'report_text', 'worker', 'fixed', 'fix_date']

    task_text = tables.Column(linkify=("logger:task-update", [tables.A("pk")]))
    pub_date = tables.DateColumn(format='d.m.Y')
    # order_date = tables.DateColumn(format='d.m.Y')
    fix_date = tables.DateColumn(format='d.m.Y')


class AddressTable(tables.Table):
    class Meta:
        model = Address
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['street', 'house', 'entrance']

    street = tables.Column(linkify=("logger:address-update", [tables.A("pk")]))


class ElevatorTable(tables.Table):
    class Meta:
        model = Elevator
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['address', 'note']

    address = tables.Column(linkify=("logger:elevator-update", [tables.A("pk")]))
