from django.contrib import admin
from .models import Profile, Stock, CartItems, ShoppingListItems
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Profile)

class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = UserField = ['username','first_name','last_name','email']
    inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Stock)
admin.site.register(CartItems)
admin.site.register(ShoppingListItems)