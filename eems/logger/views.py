from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Claim, Address, Task, Elevator
from django.views import generic
from django.urls import reverse_lazy
from .forms import (ClaimForm, AddressForm, ElevatorForm, TaskForm, OtherClaimForm)
from .tables import (ClaimTable, TaskTable, AddressTable, ElevatorTable, OtherClaimTable)
from django_tables2 import RequestConfig, SingleTableView
from datetime import datetime
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin, SingleTableView
from .filters import ClaimFilter, TaskFilter, ElevatorFilter, AddressFilter
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core import paginator
from django.contrib.auth.decorators import login_required


def new_claim(request):
    title_post = "Добавить заявку"
    button_post = "Добавить"
    title_page = 'Новая заявка по лифтам'

    if request.method != "POST":
        # initial_data = {
        #     'pub_date': datetime.now(),
        # }
        # initial = initial_data
        form = ClaimForm()
        return render(request, "new_object.html", {
            "form": form,
            "title_post": title_post,
            "button_post": button_post,
            'title_page': title_page,
        })

    form = ClaimForm(request.POST)
    if not form.is_valid():
        return render(request, "new_object.html", {
            "form": form,
            "title_post": title_post,
            "button_post": button_post,
            'title_page': title_page,
        })

    claim = form.save(commit=False)
    claim.author = request.user
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

    return render(request, "new_object.html",
                  {"form": form,
                   "claim": claim,
                   "title_post": title_post,
                   "button_post": button_post})


class FilteredElevatorClaimListView(SingleTableMixin, FilterView):
    table_class = ClaimTable
    template_name = "index.html"
    filterset_class = ClaimFilter
    paginate_by = 20

    def get_queryset(self):
        qs = Claim.objects.exclude(elevator=None)
        return qs


class FilteredOtherClaimListView(SingleTableMixin, FilterView):
    table_class = OtherClaimTable
    template_name = "index.html"
    filterset_class = ClaimFilter
    paginate_by = 20

    def get_queryset(self):
        qs = Claim.objects.filter(elevator=None)
        return qs


class NewOtherClaim(CreateView):
    model = Claim
    template_name = 'new_object.html'
    form_class = OtherClaimForm
    success_url = reverse_lazy('logger:other_claims')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        task.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_post'] = 'Добавить'
        context['title_post'] = 'Добавить заявку'
        return context


class OtherClaimUpdate(UpdateView):
    model = Claim
    template_name = 'new_object.html'
    form_class = OtherClaimForm
    success_url = reverse_lazy('logger:other_claims')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_post'] = 'Сохранить'
        context['title_post'] = 'Редактирование заявки'
        return context


class FilteredTaskListView(SingleTableMixin, FilterView):
    table_class = TaskTable
    model = Task
    template_name = "index.html"
    filterset_class = TaskFilter
    paginate_by = 20


class FilteredAddressListView(SingleTableMixin, FilterView):
    table_class = AddressTable
    model = Address
    template_name = "index.html"
    filterset_class = AddressFilter
    paginate_by = 20


class FilteredElevatorListView(SingleTableMixin, FilterView):
    table_class = ElevatorTable
    model = Elevator
    template_name = "index.html"
    filterset_class = ElevatorFilter
    paginate_by = 20


class ClaimDetailView(generic.DetailView):
    model = Claim
    template_name = 'claim_detail.html'


class AddressDetailView(generic.DetailView):
    model = Address
    template_name = 'address_detail.html'


def new_address(request):
    title_post = "Добавить адрес"
    button_post = "Добавить"

    if request.method != "POST":
        form = AddressForm()
        return render(request, "new_object.html", {
            "form": form,
            "title_post": title_post,
            "button_post": button_post
        })

    form = AddressForm(request.POST)
    if not form.is_valid():
        return render(request, "new_object.html", {
            "form": form,
            "title_post": title_post,
            "button_post": button_post
        })

    claim = form.save(commit=False)
    claim.save()
    return redirect("logger:index")


def new_elevator(request):
    title_post = "Добавить лифт"
    button_post = "Добавить лифт"

    if request.method != "POST":
        form = ElevatorForm()
        return render(request, "new_object.html", {
            "form": form,
            "title_post": title_post,
            "button_post": button_post
        })

    form = ElevatorForm(request.POST)
    if not form.is_valid():
        return render(request, "new_object.html", {
            "form": form,
            "title_post": title_post,
            "button_post": button_post
        })

    claim = form.save(commit=False)
    claim.save()
    return redirect("logger:index")


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'new_object.html'
    form_class = TaskForm
    success_url = reverse_lazy('logger:tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_post'] = 'Сохранить'
        context['title_post'] = 'Редактирование плана'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class NewTask(CreateView):
    model = Task
    template_name = 'new_object.html'
    form_class = TaskForm
    success_url = reverse_lazy('logger:tasks')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        task.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_post'] = 'Добавить'
        context['title_post'] = 'Добавить в план'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs
