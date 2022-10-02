from django.contrib import admin
from django.urls import path
# now import the views.py file into this code
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
