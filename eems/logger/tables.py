import django_tables2
from .models import Claim


class ClaimTable(django_tables2.Table):
    class Meta:
        model = Claim
        template_name = 'django_tables2/bootstrap.html'
