import re

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.http.request import split_domain_port
from django.utils.translation import gettext_lazy as _


class Agent(models.Model):
     name = models.CharField(_("Name"), blank=True, null=True, max_length=200)
     parent = models.ForeignKey(
        "pyramid.Agent",
        blank=True,
        null=True,
        verbose_name=_("Parent"),
        on_delete=models.SET_NULL,
    )

class Product(models.Model):
    name = models.CharField(_("Name"), blank=True, null=True, max_length=200)


class Pyramid(models.Model):
    name = models.CharField(_("Name"), blank=True, null=True, max_length=200)


class Threshold(models.Model):
    level = models.IntegerField(_("Level"), null=False)
    amount = models.IntegerField(_("Amount"), null=False)