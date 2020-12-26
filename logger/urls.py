from django.urls import path, re_path
from . import views
from . import dalviews
from django.contrib.auth.decorators import login_required

app_name = 'logger'
urlpatterns = [
    # urls для обработки заявок по лифтам
    path(
        '',
        login_required(views.FilteredClaimListView.as_view()),
        name='index'),
    path(
        'new_claim/',
        login_required(views.NewClaimView.as_view()),
        name='new_claim'),
    path(
        'claims/<int:pk>/',
        login_required(views.ClaimUpdateView.as_view()),
        name='claim_edit'),

    # urls для обработки прочих заявок
    path(
        'other_claims/',
        login_required(views.FilteredOtherClaimListView.as_view()),
        name='other_claims'),
    path(
        'other_claims/<int:pk>/',
        login_required(views.OtherClaimUpdate.as_view()),
        name='other_claim_edit'),
    path(
        'new_other_claim/',
        login_required(views.NewOtherClaim.as_view()),
        name='new_other_claim'),

    # urls для работы с адресами
    path(
        'new_address/',
        login_required(views.NewAddressView.as_view()),
        name='new_address'),
    path(
        'addresses/',
        login_required(views.FilteredAddressListView.as_view()),
        name='addresses'),

    # urls для работы с лифтами
    path(
        'new_elevator/',
        login_required(views.NewElevatorView.as_view()),
        name='new_elevator'),
    path(
        'elevators/',
        login_required(views.FilteredElevatorListView.as_view()),
        name='elevators'),

    # urls для работы с планами механиков
    path(
        'new_task/',
        login_required(views.NewTask.as_view()), name='new_task'),
    path(
        'tasks/',
        login_required(views.FilteredTaskListView.as_view()),
        name='tasks'),
    path(
        'tasks/<int:pk>/',
        login_required(views.TaskUpdate.as_view()),
        name='task-update'),

    # Django autocomplete light
    re_path(
        r'^address-autocomplete/$',
        dalviews.AddressAutocomplete.as_view(create_field='street'),
        name='address-autocomplete'),
    re_path(
        r'^user-autocomplete/$',
        dalviews.UserAutocomplete.as_view(),
        name='user-autocomplete'),
    re_path(
        r'^elevator-autocomplete/$',
        dalviews.ElevatorAutocomplete.as_view(),
        name='elevator-autocomplete'),
]
