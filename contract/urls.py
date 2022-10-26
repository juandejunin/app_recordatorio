from django.urls import path

from contract.views import *
from . import views

urlpatterns = [
	# Contract views
	path('', views.apiOverview, name="api-overview"),
	path('contract-list', views.ContractList, name="contract-list"),
	path('contract-detail/<str:pk>', views.ContractDetail, name="contract-detail"),
	path('contract-create', views.ContractCreate, name="contract-create"),
	path('contract-update/<str:pk>', views.ContractUpdate, name="contract-update"),
	path('contract-delete/<str:pk>', views.ContractDelete, name="contract-delete"),
]