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

     created = models.DateTimeField(auto_now_add=True, editable=False)
     updated = models.DateTimeField(auto_now=True, editable=False)

     def __repr__(self):
         return self.name

     def __str__(self):
         return self.name

class Product(models.Model):
    name = models.CharField(_("Name"), blank=True, null=True, max_length=200)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Pyramid(models.Model):
    name = models.CharField(_("Name"), blank=True, null=True, max_length=200)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)


class Threshold(models.Model):
    level = models.IntegerField(_("Level"), null=False)
    amount = models.IntegerField(_("Amount"), null=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)


class Transaction(models.Model):
    agent = models.ForeignKey(
        "pyramid.Agent",
        blank=True,
        null=True,
        verbose_name=_("Agent"),
        on_delete=models.SET_NULL,
    )
    product = models.ForeignKey(
        "pyramid.Product",
        blank=True,
        null=True,
        verbose_name=_("Product"),
        on_delete=models.SET_NULL,
    )
    amount = models.IntegerField(_("Amount"), null=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __repr__(self):
        return f"{self.agent}({self.product})({self.amount})"

    def __str__(self):
        return f"{self.agent}({self.product})({self.amount})"


class Payment(models.Model):
    agent = models.ForeignKey(
        "pyramid.Agent",
        blank=True,
        null=True,
        verbose_name=_("Agent"),
        on_delete=models.SET_NULL,
    )
    amount = models.IntegerField(_("Amount"), null=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)