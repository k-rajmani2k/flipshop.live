from django.contrib import admin
from digishop.models import ProductImages, Product, User, Payment
from django.utils.html import format_html


class ProductImageModel(admin.StackedInline):
    model = ProductImages


class ProductModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_description', 'get_price', 'get_discount', 'get_sale_price', 'file', 'thumbnail']

    inlines = [ProductImageModel]

    def get_sale_price(self, obj):
        return 'INR ' + str((obj.price) - (obj.price * (obj.discount / 100)))

    def get_description(self, obj):
        return format_html(f'<span title="{obj.description}">{obj.description[0:50]}....</span>')

    def get_price(self, obj):
        return 'INR ' + str(obj.price)

    def get_discount(self, obj):
        return str(obj.discount) + " %"

    get_sale_price.short_description = "Sale Price"
    get_discount.short_description = "Discount"
    get_price.short_description = "Original Price"


admin.site.register(Product, ProductModel)
admin.site.register(User)
admin.site.register(Payment)
