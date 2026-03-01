from django.urls import path
from . import views

urlpatterns = [
    path('', views.MarcaListView.as_view(), name='marca_list'),
    path('nova/', views.MarcaCreateView.as_view(), name='marca_create'),
    path('editar/<int:pk>/', views.MarcaUpdateView.as_view(), name='marca_update'),
    path('esborrar/<int:pk>/', views.MarcaDeleteView.as_view(), name='marca_delete'),
]

