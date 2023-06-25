from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from shop_app.models import Contact, Comment, Newsletter, Customer, Item, Category, TargetCustomer, Brand, TrendingItemCategory

admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Newsletter)
admin.site.register(Customer)


# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(TargetCustomer)
admin.site.register(Item)
admin.site.register(TrendingItemCategory)

class ItemAdmin(SummernoteModelAdmin):
    summernote_fields = ('detail',)