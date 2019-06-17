from django.views.generic.edit import FormView
from . import forms
import logging
from django.contrib.auth import login, authenticate
from django.contrib import messages

logger = logging.getLogger(__name__)


class ContactUsView(FormView):
    template_name = "contact/contacts.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


