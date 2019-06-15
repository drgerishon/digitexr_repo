from django.urls import path, include
from . import views
app_name = 'accounts'

urlpatterns = [

    path('login/', views.login_user, name='login'),
    path('success/', views.success_page, name='success'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

]
