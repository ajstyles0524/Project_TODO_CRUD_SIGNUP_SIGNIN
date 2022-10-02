from django.contrib import admin
from django.urls import path
from TODO.views import save_info
from TODO.views import index
from TODO.views import Delete

urlpatterns = [
    path('save-info/', save_info, name='save-info'),
    path('index/', index, name='index'),
    path('Delete/<int:id>', Delete, name='Delete'),
]
