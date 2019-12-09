from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('profile/', views.redirect_to_user, name='user_redirect'),
    re_path('profile/(?P<pk>\d+)/$', views.UserProfile.as_view(), name='user_detail'),
    path('', include('django.contrib.auth.urls')),
    path('register1/', views.SignUp.as_view(), name='register1'),
    path('register/', views.create_user, name='register'),

]