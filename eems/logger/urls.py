from django.urls import path, re_path

from . import views
from . import dalviews

app_name = 'logger'
urlpatterns = [
    path('', views.FilteredClaimListView.as_view(), name='index'),
    path('<int:pk>/', views.ClaimDetailView.as_view(), name='claim_detail'),
    path('new_address/', views.new_address, name='new_address'),
    path('address/<int:pk>/', views.AddressDetailView.as_view(), name='address_detail'),
    path('new_claim/', views.new_claim, name='new_claim'),
    path('<int:claim_id>/edit/', views.claim_edit, name='claim_edit'),
    path('new_elevator/', views.new_elevator, name='new_elevator'),
    path('new_task/', views.new_task, name='new_task'),
    path('tasks/', views.FilteredTaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    re_path(
        r'^address-autocomplete/$',
        dalviews.AddressAutocomplete.as_view(create_field='street'),
        name='address-autocomplete'
    ),
]
