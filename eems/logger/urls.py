from django.urls import path

from . import views

app_name = 'logger'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ClaimDetailView.as_view(), name='claim_detail'),
    path('address/<int:pk>/', views.AddressDetailView.as_view(), name='address_detail'),
    path('new_claim/', views.new_claim, name='new_claim'),
    path('<int:claim_id>/edit/', views.claim_edit, name='claim_edit'),
]
