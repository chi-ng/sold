from django.contrib import admin

from .models import PageView

# models
from .models import Item, Bid

# Register your models here.


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

admin.site.register(PageView, PageViewAdmin)

admin.site.register(Item)
admin.site.register(Bid)
