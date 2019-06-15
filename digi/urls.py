from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.HomePage.as_view(template_name="index.html"), name='index'),
    path('accounts/', include("accounts.urls")),

]