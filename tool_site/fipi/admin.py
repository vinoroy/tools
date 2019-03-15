from django.contrib import admin
from .models import Asset, Portfolio

admin.site.register(Portfolio)
admin.site.register(Asset)

