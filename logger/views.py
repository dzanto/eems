from .models import Claim, Address, Task, Elevator
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import ClaimFilter, TaskFilter, ElevatorFilter, AddressFilter
from django.views.generic.edit import CreateView, UpdateView
from .forms import (
    ClaimForm, AddressForm, ElevatorForm, TaskForm, OtherClaimForm
)
from .tables import (
    ClaimTable, TaskTable, AddressTable, ElevatorTable, OtherClaimTable
)


class NewClaimView(CreateView):
    """
    View для создания заявки по лифтам
    """
    model = Claim
    template_name = 'new_object.html'
    form_class = ClaimForm
    success_url = reverse_lazy('logger:index')

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


class ClaimUpdateView(UpdateView):
    model = Claim
    template_name = 'new_object.html'
    form_class = ClaimForm
    success_url = reverse_lazy('logger:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_post'] = 'Сохранить'
        context['title_post'] = 'Редактирование заявки'
        return context


class FilteredClaimListView(SingleTableMixin, FilterView):
    table_class = ClaimTable
    template_name = "index.html"
    filterset_class = ClaimFilter
    paginate_by = 20

    def get_queryset(self):
        qs = Claim.objects.exclude(elevator=None)
        return qs


class NewOtherClaim(CreateView):
    """
    View для создания прочих заявок
    """
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


class FilteredOtherClaimListView(SingleTableMixin, FilterView):
    table_class = OtherClaimTable
    template_name = "index.html"
    filterset_class = ClaimFilter
    paginate_by = 20

    def get_queryset(self):
        qs = Claim.objects.filter(elevator=None)
        return qs


class NewAddressView(CreateView):
    model = Address
    template_name = 'new_object.html'
    form_class = AddressForm
    success_url = reverse_lazy('logger:addresses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_post'] = 'Добавить адрес'
        context['title_post'] = 'Добавить адрес'
        return context


class UpdateAddressView(UpdateView):
    model = Address
    template_name = 'new_object.html'
    form_class = AddressForm
    success_url = reverse_lazy('logger:addresses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_post'] = 'Изменить адрес'
        context['button_post'] = 'Сохранить'

        return context


class FilteredAddressListView(SingleTableMixin, FilterView):
    table_class = AddressTable
    model = Address
    template_name = "index.html"
    filterset_class = AddressFilter
    paginate_by = 20


class NewElevatorView(CreateView):
    model = Elevator
    template_name = 'new_object.html'
    form_class = ElevatorForm
    success_url = reverse_lazy('logger:elevators')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_post'] = 'Добавить лифт'
        context['title_post'] = 'Добавить лифт'
        return context


class UpdateElevatorView(UpdateView):
    model = Elevator
    template_name = 'new_object.html'
    form_class = ElevatorForm
    success_url = reverse_lazy('logger:elevators')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_post'] = 'Редактирование данных о лифте'
        context['button_post'] = 'Сохранить'

        return context


class FilteredElevatorListView(SingleTableMixin, FilterView):
    table_class = ElevatorTable
    model = Elevator
    template_name = "index.html"
    filterset_class = ElevatorFilter
    paginate_by = 20


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


class FilteredTaskListView(SingleTableMixin, FilterView):
    table_class = TaskTable
    model = Task
    template_name = "index.html"
    filterset_class = TaskFilter
    paginate_by = 20
