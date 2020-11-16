from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Claim, Address
from django.views import generic
from django.urls import reverse
from .forms import ClaimForm, AddressForm
from .tables import ClaimTable
from django_tables2 import RequestConfig, SingleTableView
from datetime import datetime
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import ClaimFilter


def new_claim(request):
    title_post = "Добавить заявку"
    button_post = "Добавить"

    if request.method != "POST":
        # initial_data = {
        #     'pub_date': datetime.now(),
        # }
        # initial = initial_data
        form = ClaimForm()
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


class FilteredClaimListView(SingleTableMixin, FilterView):
    table_class = ClaimTable
    model = Claim
    template_name = "logger/index.html"
    filterset_class = ClaimFilter


class ClaimDetailView(generic.DetailView):
    model = Claim
    template_name = 'logger/claim_detail.html'


class AddressDetailView(generic.DetailView):
    model = Address
    template_name = 'logger/address_detail.html'


def new_address(request):
    title_post = "Добавить адрес"
    button_post = "Добавить"

    if request.method != "POST":
        form = AddressForm()
        return render(request, "logger/new_address.html", {
            "form": form,
            "title_post": title_post,
            "button_post": button_post
        })

    form = AddressForm(request.POST)
    if not form.is_valid():
        return render(request, "logger/new_address.html", {
            "form": form,
            "title_post": title_post,
            "button_post": button_post
        })

    claim = form.save(commit=False)
    claim.save()
    return redirect("logger:index")
