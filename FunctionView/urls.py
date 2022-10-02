from django.urls import path
# now import the views.py file into this code
from . import views

urlpatterns = [
    path('', views.index),
    path('view/', views.create_view),
    path('list-view/', views.list_view),
    path('<id>', views.detail_view),
    path('<id>/update', views.update_view),
    path('<id>/delete', views.delete_view),
]
