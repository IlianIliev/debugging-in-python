from django.shortcuts import render, redirect

from contacts.forms import ContactForm
from contacts.models import Contact
from contacts.utils import get_latest_hash


def list(request):
    contacts = Contact.objects.filter(owner=request.user)
    return render(request, 'contacts/list.html', {'contacts': contacts})


def create(request):
    form = ContactForm(request, request.POST or None)
    if form.is_valid():
        contact = form.save()

        request.session['latest_hash'] = contact.get_hash()
        return redirect('contacts:list')

    return render(request, 'contacts/create.html', context={'form': form})


def resync(request):
    latest_hash = get_latest_hash()
    request.session['latest_hash'] = latest_hash
    return redirect('contacts:list')
