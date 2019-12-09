from django.urls import path, re_path
from . import views


urlpatterns = [
   path('', views.intropage, name='intro'),
   path('homepage/', views.homepage, name='home'),
   path('homepage/vehicles/', views.VehicleList.as_view(), name='vehicles'),
   path('create/', views.VehicleCreate.as_view(), name='create'),
   path('detail/<int:pk>/', views.VehicleDetail.as_view(), name='detail'),
   path('user_list/', views.UserVehicles.as_view(), name='user_list'),
   path('delete/<int:pk>/', views.VehicleDelete.as_view(), name='delete'),
   path('edit/<int:pk>/', views.VehicleUpdate.as_view(), name='edit'),
   path('get_all_users/', views.GetAllUsers.as_view(), name='get_all_users'),
   path('user_list2/<int:pk>/', views.UserVehicles2.as_view(), name='user_list2'),
   path('about/', views.about, name='about'),

]
