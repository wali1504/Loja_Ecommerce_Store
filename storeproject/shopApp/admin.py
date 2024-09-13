from django.contrib import admin

from shopApp.models import user ,AddProduct


class customizeAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','username','email','password')

class customizeProducts(admin.ModelAdmin):
    list_display=('ProductName','Description','Category','Price','StockQuantity')
admin.site.register(user,customizeAdmin)

admin.site.register(AddProduct,customizeProducts)
