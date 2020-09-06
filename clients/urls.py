from django.urls import path
from . import views
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    VehicleUpdateView,
    VehicleDeleteView,
    VehicleCreateView,
    CommentCreateView
)


urlpatterns = [
    path('<int:pk>/edit/',ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/vehicle/edit/',VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('<int:pk>/vehicle/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('', ClientListView.as_view(), name='client_list'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('comment/new/<int:pk>', CommentCreateView.as_view(), name='comment_new'),
    path('vehicle/new/<int:pk>', VehicleCreateView.as_view(), name='vehicle_new'),
]
