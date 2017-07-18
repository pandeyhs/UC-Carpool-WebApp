#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from django.forms import ModelForm,Textarea
from django.utils.translation import ugettext_lazy as _

from home.models import Contact




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
        'content': Textarea(attrs={'cols': 120, 'rows': 10}),
        }
        labels = {
        "contact_name": _("Name"),
        "contact_email":_("Email"),
        "content":_("Message"),

        }
        '''
        contact_name = forms.CharField(required=True)
        contact_email = forms.EmailField(required=True)
        content = forms.CharField(
        required=True,
        widget=forms.Textarea
        )

        # the new bit we're adding
        def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['contact_name'].label = "Your name:"
            self.fields['contact_email'].label = "Your email:"
            self.fields['content'].label = "What do you want to say?"
            '''
