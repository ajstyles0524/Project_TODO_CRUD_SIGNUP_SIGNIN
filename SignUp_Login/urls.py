from django.contrib import admin
from django.urls import path, include
from . import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [

    path('admin/', admin.site.urls),
    path('hello/', user_view.hello),
    path('', user_view.index, name='index'),
    path('login/', user_view.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/temp.html'), name='logout'),
    path('register/', user_view.register, name='register'),
]
