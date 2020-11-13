from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Claim, Address
from django.views import generic
from django.urls import reverse


class IndexView(generic.ListView):
    template_name = 'logger/index.html'
    context_object_name = 'latest_claims'

    def get_queryset(self):
        return Claim.objects.order_by('-pub_date')[:5]


class ClaimDetailView(generic.DetailView):
    model = Claim
    template_name = 'logger/claim_detail.html'


class AddressDetailView(generic.DetailView):
    model = Address
    template_name = 'logger/address_detail.html'


# def index(request):
#     latest_claims = Claim.objects.order_by('-pub_date')[:5]
#     addresses = Address.objects.all()
#     context = {
#         'latest_claims': latest_claims,
#         'addresses': addresses,
#     }
#     return render(request, 'logger/index.html', context)
#
#
# def detail(request, claim_id):
#     claim = get_object_or_404(Claim, pk=claim_id)
#     return render(request, 'logger/claim_detail.html', {'claim': claim})
#
#
# def address_detail(request, address_id):
#     address = get_object_or_404(Address, pk=address_id)
#     return render(request, 'logger/address_detail.html', {'address': address})

