import django_tables2 as tables
from django_tables2.utils import A
from .models import Claim, Task
from .filters import ClaimFilter


class ClaimTable(tables.Table):
    class Meta:
        model = Claim
        template_name = 'django_tables2/bootstrap.html'

    claim_text = tables.Column(linkify=("logger:claim_edit", [tables.A("pk")]))
    # address_filter = ClaimFilter
    # address = tables.Column(linkify=("logger:address_detail", [tables.A("address__pk")]))
    # address = tables.Column(linkify=("logger:index", {"address__street": tables.A("address__street")}))
            #                 , {"filter.address__street": tables.A(
            # "address__street")})
    pub_date = tables.DateTimeColumn(format='d.m.Y G:i')
    fix_date_time = tables.DateColumn(format='d.m.Y G:i')


class TaskTable(tables.Table):
    class Meta:
        model = Task
        template_name = 'django_tables2/bootstrap.html'

    task_text = tables.Column(linkify=("logger:task-update", [tables.A("pk")]))
    pub_date = tables.DateColumn(format='d.m.Y')
    fix_date = tables.DateColumn(format='d.m.Y')

