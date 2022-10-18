from django.urls import path

from usuario.views import *
from . import views

urlpatterns = [
	# Auth views
	path('auth/login', LoginAPIView.as_view(), name='auth_login'),

	# User views
	path('', views.apiOverview, name="api-overview"),
	path('user-list', views.UserList, name="user-list"),
	path('user-detail/<str:pk>', views.UserDetail, name="user-detail"),
	path('user-create', views.UserCreate, name="user-create"),
	path('user-update/<str:pk>', views.UserUpdate, name="user-update"),
	path('user-delete/<str:pk>', views.UserDelete, name="user-delete"),
]