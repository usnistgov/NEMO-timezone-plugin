from NEMO.models import UserPreferences, Tool
from django.db import models


common_timezones = [
    "US/Alaska",
    "US/Arizona",
    "US/Central",
    "US/Eastern",
    "US/Hawaii",
    "US/Mountain",
    "US/Pacific",
    "UTC",
]


class UserPreferencesTimezone(models.Model):
    user_preferences = models.OneToOneField(UserPreferences, on_delete=models.CASCADE, related_name="timezone")
    timezone = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        choices=[(tz, tz) for tz in common_timezones],
        help_text="Select the user's timezone",
    )

    def __str__(self):
        return self.timezone or ""

    class Meta:
        verbose_name = "Timezone"
        verbose_name_plural = "Timezone"


class ToolTimezone(models.Model):
    tool = models.OneToOneField(Tool, on_delete=models.CASCADE, related_name="timezone")
    timezone = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        choices=[(tz, tz) for tz in common_timezones],
        help_text="Select the tool's timezone",
    )

    def __str__(self):
        return self.timezone or ""

    class Meta:
        verbose_name = "Timezone"
        verbose_name_plural = "Timezone"
