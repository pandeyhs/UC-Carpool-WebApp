# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from home.forms import ContactForm
from django.template.loader import render_to_string

def index(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.contact_name = request.POST.get(
            'contact_name'
            , '')
            contact.contact_email = request.POST.get(
            'contact_email'
            , '')
            contact.form_content = request.POST.get('content', '')
            contact.save()
            '''
            cemetery.name=request.name
            cemetery.city=request.city
            cemetery.zipcode=request.zipcode
            cemetery.created_by=request.user
            cemetery.date_created=timezone.now()
            cemetery.save()
            # Email the profile with the
            # contact information
            template = get_template('home/contact_template.txt')
            ctx = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
            }
            content = render_to_string('home/contact_template.txt',ctx)

            email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" +'',
            ['pandeyhs@mail.uc.edu'],
            headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('index')
            '''
    else:
            form=ContactForm
    return render(request, 'home/home.html', {
        'form': form_class,
        })
        #    return render(request, 'home/home.html')



