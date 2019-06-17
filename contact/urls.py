from django.urls import path

from . import views
from django.views.generic import TemplateView

app_name = 'contact'

urlpatterns = [
    path("", views.ContactUsView.as_view(), name="contact", ),
    path("about-us/", TemplateView.as_view(template_name="contact/about_us.html"), name="about_us", ),

]
