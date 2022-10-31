from django.urls import path
from . import views


urlpatterns = [
    path('log_in/', views.log_in_user, name='log_in'),
    path('log_out/', views.log_out_user, name='logout_user'),
    path('registration/', views.register_user, name='registration'),
]
