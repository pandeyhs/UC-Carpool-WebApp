# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    content = models.CharField(max_length=500)


    def __unicode__(self):              # __unicode__ on Python 2
            return self.contact_name
            return self.contact_email
            return self.content
