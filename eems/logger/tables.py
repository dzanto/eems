import django_tables2 as tables
from django_tables2.utils import A
from .models import Claim


class ClaimTable(tables.Table):
    class Meta:
        model = Claim
        template_name = 'django_tables2/bootstrap.html'

    claim_text = tables.Column(linkify=("logger:claim_edit", [tables.A("pk")]))
    pub_date = tables.DateTimeColumn(format='Y-m-d G:i')
