from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User

__all__ = ['UserAdmin']


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ('-id',)
    list_display_links = ('id', 'email')
    list_display = ('id', 'email', 'date_joined', 'last_login', 'is_active')
    fieldsets = (
        (None, {"fields": ("password", )}),
        (_("Personal info"), {"fields": ("email", )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
