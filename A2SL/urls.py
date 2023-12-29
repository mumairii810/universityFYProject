"""A2SL URL Configuration

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
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('about/',views.about_view,name='about'),
    # path('contact/',views.contact_view,name='contact'),
    path('contact/',views.conactfrm,name='contact'),
    
    # Other URL patterns...
    path('signup/', views.signup_final_view, name='signup_final'),
    
    
    # Other URL patterns...

    path('login/',views.login_final_view,name='login_finals'),
    path('login/', views.login_view, name='login'),
    # path('logout/',views.logout_view,name='logout'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/',views.signup_final_view,name='signup_finals'),
    path('animation/',views.animation_view,name='animation'),
    path('',views.index_view,name='index'),
    path('index/',views.index_view,name='index'),
    
    path('home/',views.home_view,name='home'),
    path('contact_form/', views.contact_form_views , name = 'contact_form'),
    path('forgotpassword/', views.forgot_password , name = 'forgot_password'),
    
    # path('animation/',views.animation_view,name='animation'),
    path('http://127.0.0.1:8000/home/',views.animation_view,name='http://127.0.0.1:8000/home'),
    path('password_recovery/',views.password_recovery_function,name='password_recovery'),
    path('forgotpassword/password_recovery/',views.password_recovery_function,name='password_recovery'),
    
    path('reset-password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset-password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

    path('accounts/', include('allauth.urls')),
    path('googlelogin/', views.google_login, name='google_login'),
    path('changeemailgooglelogin/', views.change_email_google_login, name='change_email_google_login'),
    path('login_google/',views.login_google,name='login_google'),

    path('home/', views.home_view, name='home'),

]
