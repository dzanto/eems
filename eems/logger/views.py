from django.shortcuts import render
from django.http import Http404
from .models import Claim


def index(request):
    latest_claims = Claim.objects.order_by('-pub_date')[:5]
    context = {
        'latest_claims': latest_claims,
    }
    return render(request, 'logger/index.html', context)

def detail(request, claim_id):
    try:
        claim = Claim.objects.get(pk=claim_id)
    except Claim.DoesNotExist:
        raise Http404('Заявка с данным ID не найдена')
    return render(request, 'logger/detail.html', {'claim': claim})

