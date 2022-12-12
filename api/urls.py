from django.urls import re_path
from api import views

urlpatterns=[
    re_path(r'^motorista$',views.RestApiMotorista),
    re_path(r'^motorista/([0-9]+)$',views.RestApiMotorista),
    re_path(r'^veiculo$',views.RestApiVeiculo),
    re_path(r'^veiculo$/([0-9]+)$',views.RestApiVeiculo),
    re_path(r'^controle$',views.RestApiControle),
    re_path(r'^controle$/([0-9]+)$',views.RestApiControle)

]
