from NEMO.models import User
from NEMO.views.users import user_preferences
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from NEMO_timezone.models import UserPreferencesTimezone, common_timezones


@login_required
@require_http_methods(["GET", "POST"])
def custom_user_preferences(request):
    original_response = user_preferences(request)
    user_preferences_tz_enabled = getattr(settings, "USER_PREFERENCES_TZ_ENABLED", False)
    if not user_preferences_tz_enabled:
        return original_response
    user: User = User.objects.get(pk=request.user.id)
    if request.method == "POST":
        user_timezone = request.POST.get("user_preference_tz", "")
        UserPreferencesTimezone.objects.update_or_create(
            user_preferences=user.preferences, defaults={"timezone": user_timezone}
        )
        # Redirecting so the page is completely refreshed and we can have the time updated right away
        messages.success(request, "Your preferences have been saved")
        return redirect("user_preferences")
    current_user_timezone = ""
    try:
        current_user_timezone = user.preferences.timezone.timezone
    except UserPreferencesTimezone.DoesNotExist:
        pass
    dictionary = {"user_timezone": current_user_timezone, "timezones": common_timezones}
    return render_combine_responses(request, original_response, "NEMO_timezone/user_preferences_tz.html", dictionary)


def render_combine_responses(request, original_response: HttpResponse, template_name, context):
    """ Combines contents of an original http response with a new one """
    additional_content = render(request, template_name, context)
    original_response.content += additional_content.content
    return original_response
