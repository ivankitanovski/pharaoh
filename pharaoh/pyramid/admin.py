from django.contrib import admin

from .models import Agent, Product, Pyramid, Threshold


class AgentAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")

    def save_form(self, request, form, change):
        super().save_form(request, form, change)

admin.site.register(Agent, AgentAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", )

admin.site.register(Product, ProductAdmin)


class PyramidAdmin(admin.ModelAdmin):
     pass

admin.site.register(Pyramid, PyramidAdmin)


class ThresholdAdmin(admin.ModelAdmin):
    list_display = ("level", "amount", )

admin.site.register(Threshold, ThresholdAdmin)