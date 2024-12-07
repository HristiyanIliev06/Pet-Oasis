from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserEditForm, CustomUserForm
from accounts.models import Profile

UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ('first_name', 'last_name', 'age', 'account_picture')


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    form = CustomUserEditForm
    add_form = CustomUserForm

    list_display = ('username', 'email')

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', )})
    )

