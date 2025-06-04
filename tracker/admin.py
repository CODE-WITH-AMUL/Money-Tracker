from django.contrib import admin
from .models import Card, Transaction, Notification

# Register your models here.
admin.site.register(Card)
admin.site.register(Transaction)
admin.site.register(Notification)
