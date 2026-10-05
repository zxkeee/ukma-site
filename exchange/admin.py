from django.contrib import admin
from exchange.models import ExchangeProgram


# Register your models here.

class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ["university", "languages", "places", "deadline"]


admin.site.register(ExchangeProgram, ExchangeProgramAdmin)
