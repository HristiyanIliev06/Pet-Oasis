from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from accounts.forms import UserRegisterForm, EditAccountForm
from accounts.models import Profile

UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ('first_name', 'last_name', 'age', 'account_picture')
    #readonly_fields = ('created_at', 'updated_at')
    extra = 1
    verbose_name = "User Profile"
    verbose_name_plural = "User Profiles"


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    form = EditAccountForm
    add_form = UserRegisterForm
    inlines = (ProfileInline,)

    list_display = ('username', 'email', 'is_active', 'is_staff', 'last_login', 'get_profile_picture')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'last_login')
    search_fields = ('username', 'email', 'profile__first_name', 'profile__last_name')
    ordering = ('-last_login',)
    date_hierarchy = 'last_login'
    
    def get_profile_picture(self, obj):
        if hasattr(obj, 'profile') and obj.profile.account_picture:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', 
                             obj.profile.account_picture.url)
        return "No picture"
    get_profile_picture.short_description = 'Profile Picture'

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )

    fieldsets = (
        ('Credentials', {
            'fields': ('username', 'email', 'password'),
            'classes': ('wide',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',),
            'description': 'User permission settings'
        }),
        ('Important Dates', {
            'fields': ('last_login',),
            'classes': ('collapse',),
            'description': 'User activity timestamps'
        })
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('last_login',)
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # Only for new users
            Profile.objects.create(user=obj)

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
