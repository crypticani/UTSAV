from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from main.views import signup_view, activation_sent_view, activate
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.Home, name='index'),
#     path('record', views.RecordView),
    path('Display', views.Display, name='Display'),
    path('register', signup_view, name='register'),
    path('records', views.Records, name='records'),
    path('gallery', views.Gallery, name='gallery'),
    path('contact', views.Contact, name='contact'),
    path('feedback', views.Feedback, name='feedback'),
    path("logout", views.Logout, name="logout"),
    path('user_logout', views.user_logout, name='user_logout'),
    path('accounts/profile/', views.Profile, name='profile'),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('activate/<slug:uidb64>/<slug:token>/user/login',
         auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='user/login.html'), name='login'),
    path('invalid', views.activation_invalid_view, name="activation_invalid"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='user/login.html'),
         name='login')]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
