from django.urls import path
from . import views

urlpatterns = [
    path('medshows/', views.MedShowListView.as_view(), name='medshow'),
    path('medshows/create/', views.create_medshow, name='medshows_create'),
    path('medshows/<int:id>/', views.MedShowsDetailView.as_view(), name='medshows_detail'),
    path('medshows/update/<int:id>/', views.update_medshow, name='medshows_update'),
    path('medshows/delete/<int:id>/', views.delete_medshow, name='medshows_delete'),
]
