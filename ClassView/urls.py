from django.urls import path
# now import the views.py file into this code
from . import views

urlpatterns = [
    path('', views.GeeksCreate.as_view()),
    path('view/', views.GeeksList.as_view()),
    path('<pk>/', views.GeeksDetailView.as_view()),
    path('<pk>/update', views.GeeksUpdateView.as_view()),
    path('<pk>/delete/', views.GeeksDeleteView.as_view()),
    path('form/', views.GeeksFormView.as_view()),
]
