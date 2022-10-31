from django.urls import path
from . import views

app_name = 'parse'
urlpatterns = [
    path('med-aparment-list/', views.ParserView.as_view(), name='med_apartment_list'),
    path('parser/', views.ParserFormView.as_view(), name='parse_func'),
]
