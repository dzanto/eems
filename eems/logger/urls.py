from django.urls import path, re_path

from . import views
from . import dalviews
from django.contrib.auth.decorators import login_required

app_name = 'logger'
urlpatterns = [
    path('', login_required(views.FilteredElevatorClaimListView.as_view()), name='index'),
    path('<int:pk>/', login_required(views.ClaimDetailView.as_view()), name='claim_detail'),
    path('new_claim/', login_required(views.new_claim), name='new_claim'),
    path('<int:claim_id>/edit/', login_required(views.claim_edit), name='claim_edit'),
    path('other_claims/', login_required(views.FilteredOtherClaimListView.as_view()), name='other_claims'),
    path('claims/<int:pk>/', login_required(views.OtherClaimUpdate.as_view()), name='other_claim_edit'),
    path('new_other_claim/', login_required(views.NewOtherClaim.as_view()), name='new_other_claim'),

    path('new_address/', login_required(views.new_address), name='new_address'),
    path('addresses/', login_required(views.FilteredAddressListView.as_view()), name='addresses'),
    path('address/<int:pk>/', login_required(views.AddressDetailView.as_view()), name='address_detail'),

    path('new_elevator/', login_required(views.new_elevator), name='new_elevator'),
    path('elevators/', login_required(views.FilteredElevatorListView.as_view()), name='elevators'),

    path('new_task/', login_required(views.NewTask.as_view()), name='new_task'),
    path('tasks/', login_required(views.FilteredTaskListView.as_view()), name='tasks'),
    path('tasks/<int:pk>/', login_required(views.TaskUpdate.as_view()), name='task-update'),
    re_path(
        r'^address-autocomplete/$',
        dalviews.AddressAutocomplete.as_view(create_field='street'),
        name='address-autocomplete'
    ),
    re_path(
        r'^user-autocomplete/$',
        dalviews.UserAutocomplete.as_view(),
        name='user-autocomplete'
    ),
    re_path(
        r'^elevator-autocomplete/$',
        dalviews.ElevatorAutocomplete.as_view(),
        name='elevator-autocomplete'
    ),
]
