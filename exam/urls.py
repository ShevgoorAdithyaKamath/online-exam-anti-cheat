"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from userlogin import views as user_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index', user_view.index, name="index"),
    path('admin/', admin.site.urls),
    url(r'^q/', include('quiz.urls')),
    path('home/', include('HOME.urls')),
    path("register/",
         user_view.register, name="register"),
    path("profile/", user_view.profile, name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="userlogin/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="userlogin/logout.html"),
        name="logout",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="userlogin/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="userlogin/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="userlogin/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="userlogin/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='userlogin/password_change.html'), name="password_change",
    ),
    path(
        'password-change-done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='userlogin/password_change_done.html'), name="password_change_done",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
