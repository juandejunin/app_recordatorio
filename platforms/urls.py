from django.urls import path
from platforms.views import *
from . import views

urlpatterns = [
	# Contract views
	path('', views.apiOverview, name="api-overview"),
	path('platforms-list', views.PlatforsmList, name="platforms-list"),
	path('platforms-detail/<str:pk>', views.PlatformsDetail, name="platforms-detail"),
	path('platforms-create', views.PlatformsCreate, name="platforms-create"),
	path('platforms-update/<str:pk>', views.PlatformsUpdate, name="platforms-update"),
	path('platforms-delete/<str:pk>', views.PlatformsDelete, name="platforms-delete"),
]