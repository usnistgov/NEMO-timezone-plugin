from NEMO.admin import UserPreferencesAdmin, ToolAdmin, ToolDocumentsInline
from NEMO.models import UserPreferences, User, Tool
from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe

from NEMO_timezone.models import UserPreferencesTimezone, ToolTimezone


class UserPreferencesTimezoneInline(admin.StackedInline):
    model = UserPreferencesTimezone
    can_delete = False


class NewUserPreferencesAdminForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)

    class Meta:
        model = UserPreferences
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_user(self):
        user: User = self.cleaned_data.get("user")
        if user and user.preferences:
            new_url = reverse("admin:NEMO_userpreferences_change", args=[user.preferences_id])
            raise ValidationError(
                mark_safe(
                    f'This user already has preferences saved. Click <a href="{new_url}">here</a> to go and edit them'
                )
            )
        return user


class NewUserPreferencesAdmin(UserPreferencesAdmin):
    form = NewUserPreferencesAdminForm
    inlines = (UserPreferencesTimezoneInline,)

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ("user",) if obj else self.readonly_fields

    def get_fields(self, request, obj=None):
        # moving
        form: ModelForm = self._get_form_for_get_fields(request, obj)
        form_fields = [*form.base_fields]
        readonly_fields = [*self.get_readonly_fields(request, obj)]
        if "user" in form_fields:
            form_fields.remove("user")
        if "user" in readonly_fields:
            readonly_fields.remove("user")
        return ["user", *form_fields, *readonly_fields]

    def save_model(self, request, obj: UserPreferences, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            user = form.cleaned_data["user"]
            user.preferences = obj
            user.save()


class ToolTimezoneInline(admin.StackedInline):
    model = ToolTimezone
    can_delete = False


class NewToolAdmin(ToolAdmin):
    inlines = [ToolTimezoneInline] + ToolAdmin.inlines


# Re-register UserPreferences
admin.site.unregister(UserPreferences)
admin.site.register(UserPreferences, NewUserPreferencesAdmin)

# Re-register Tool
admin.site.unregister(Tool)
admin.site.register(Tool, NewToolAdmin)
