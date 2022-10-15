from django.urls import path

from autenticar_correo  import views

urlpatterns = [
    path('', views.send.as_view(), name='send'),
    # path('verificacodigo/', views.verificacodigo.as_view(), name='verificacodigo')
    path('verificar/', views.verificacion.as_view(), name='verificacion'),
    
]
