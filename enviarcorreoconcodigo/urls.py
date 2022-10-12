from django.urls import path

from enviarcorreoconcodigo  import views

urlpatterns = [
    path('', views.Send.as_view(), name='send'),
]
