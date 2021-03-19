import re
from datetime import datetime

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
        verbose_name=_("Mentor"),
        on_delete=models.SET_NULL,
    )
    points = models.FloatField(_("Points"), default=0)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Level(models.Model):
    level = models.IntegerField(_("Level"), primary_key=True)
    name = models.CharField(_("Name"), blank=True, null=True, max_length=200)

    points_from = models.FloatField(_("Points From"), default=0)
    points_to = models.FloatField(_("Points To"), default=0)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __repr__(self):
        return f"{self.level}"

    def __str__(self):
        return f"{self.level}"


class Product(models.Model):
    name = models.CharField(_("Name"), blank=True, null=True, max_length=200)

    coefficient = models.FloatField(_("Points coefficient"), blank=True, null=True)

    adds_to_points = models.BooleanField(_("Adds to points"), default=True)
    adds_to_payment = models.BooleanField(_("Adds to payment"), default=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


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

    created = models.DateTimeField(auto_now_add=True, editable=True)
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
    amount = models.FloatField(_("Amount"), null=False)
    month = models.DateTimeField(default=datetime.now, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)