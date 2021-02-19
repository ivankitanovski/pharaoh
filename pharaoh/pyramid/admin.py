from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _

from .models import Agent, Product, Pyramid, Threshold, Transaction, Payment
from .utils import calculate_payments_for_agents


class AgentAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")

    # def save_form(self, request, form, change):
    #     super().save_form(request, form, change)

admin.site.register(Agent, AgentAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", )

admin.site.register(Product, ProductAdmin)


class PyramidAdmin(admin.ModelAdmin):
     pass

admin.site.register(Pyramid, PyramidAdmin)


class ThresholdAdmin(admin.ModelAdmin):
    list_display = ("level", "amount",)

admin.site.register(Threshold, ThresholdAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("agent", "product", "amount", "created",)

admin.site.register(Transaction, TransactionAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("agent", "amount", "created",)

    change_list_template = "admin/pyramid/payment/change_list.html"

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [path(
                "calculate-payments/",
                self.admin_site.admin_view(self.calculate_payments),
                name="calculate-payments",
            ),]

        return custom_urls + urls

    def calculate_payments(self, request):
        messages.info(
            request,
            str(calculate_payments_for_agents())
        )
        return redirect("admin:pyramid_payment_changelist")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Payment, PaymentAdmin)