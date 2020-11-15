from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Claim, Address
from django.views import generic
from django.urls import reverse
from .forms import ClaimForm
from .tables import ClaimTable
from django_tables2 import RequestConfig, SingleTableView
from datetime import datetime


def new_claim(request):
    title_post = "Добавить заявку"
    button_post = "Добавить"

    if request.method != "POST":
        initial_data = {
            'pub_date': datetime.now(),
        }
        form = ClaimForm(initial=initial_data)
        return render(request, "logger/new_claim.html", {
            "form": form,
            "title_post": title_post,
            "button_post": button_post
        })

    form = ClaimForm(request.POST)
    if not form.is_valid():
        return render(request, "logger/new_claim.html", {
            "form": form,
            "title_post": title_post,
            "button_post": button_post
        })

    claim = form.save(commit=False)
    # post.author = request.user
    claim.save()
    return redirect("logger:index")


def claim_edit(request, claim_id):
    claim = get_object_or_404(Claim, id=claim_id)

    title_post = "Редактировать запись"
    button_post = "Сохранить запись"

    form = ClaimForm(request.POST or None, instance=claim)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect("logger:index")

    return render(request, "logger/new_claim.html",
                  {"form": form,
                   "claim": claim,
                   "title_post": title_post,
                   "button_post": button_post})


class IndexView(SingleTableView):
    model = Claim
    table_class = ClaimTable
    template_name = 'logger/index.html'


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

