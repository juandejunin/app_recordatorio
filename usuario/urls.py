from django.urls import path

from usuario.views import *
from . import views

urlpatterns = [
    # path('', UserListView.as_view(), name='user_list'),
    # path('add/', UserCreateView.as_view(), name='user_create'),
    # path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update')
    # path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete')
    path('', views.apiOverview, name="api-overview"),
	path('user-list', views.UserList, name="user-list"),
	path('user-detail/<str:pk>', views.UserDetail, name="user-detail"),
	path('user-create', views.UserCreate, name="user-create"),

	path('user-update/<str:pk>', views.UserUpdate, name="user-update"),
	path('user-delete/<str:pk>', views.UserDelete, name="user-delete"),
]