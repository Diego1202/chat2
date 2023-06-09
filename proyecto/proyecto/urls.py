"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuario import views, context_processors
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'usuario.views.error_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/sign-up/', views.register, name='register'),
    path('auth/sign-in/', views.login_view, name='login'),
    path('auth/logout/', views.logout.as_view(), name='logout'),
    path('auth/user/update/', views.profile_update, name='update'),
    path('chat/', views.chat, name='chat'),
    path('json/perfiles/', context_processors.profiles_with_messages, name='profile_messages'),
    path('chat/<str:username>/', views.message_view, name='chat-user'),
    path('json/<str:username>/', views.message_json, name='chatJson'),
    path('auth/pasword-change/', views.change_password, name='password_change'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)