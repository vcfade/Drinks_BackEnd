from django.contrib import admin
from .models import Clientes, Roles, User
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('role',)}),
    )


admin.site.register(User, MyUserAdmin)



# Register your models into de django admin here.
admin.site.register(Clientes)
admin.site.register(Roles)
