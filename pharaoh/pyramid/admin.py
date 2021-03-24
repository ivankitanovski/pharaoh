from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _

from .models import Agent, Product, Level, Transaction, Payment
from .utils import calculate_payments_for_agents


class AgentAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "points", "level")
    search_fields = ("name", )

    def level(self, obj):
        if obj and obj.points:
            return Level.objects.filter(points_to__gt=obj.points).order_by("level").first()
        return "-"

    level.short_description = _("Level")
    level.admin_order_field = "points"

    # def save_form(self, request, form, change):
    #     super().save_form(request, form, change)

admin.site.register(Agent, AgentAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "coefficient", "points_type",)
    list_filter = ("points_type",)

admin.site.register(Product, ProductAdmin)


class LevelAdmin(admin.ModelAdmin):
    list_display = ("level", "name", "points_from", "points_to",)

admin.site.register(Level, LevelAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("agent", "product", "amount", "created",)

admin.site.register(Transaction, TransactionAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("agent", "for_month", "production_points", "reward_points", "fiscal_points", "career_points", "compensation")

    change_list_template = "admin/pyramid/payment/change_list.html"

    def for_month(self, obj):
        return obj.created.strftime("%m.%Y")

    for_month.admin_order_field = 'created'
    for_month.short_description = 'Month'

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

admin.site.register(Payment, PaymentAdmin)