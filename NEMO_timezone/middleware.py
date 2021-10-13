import pytz
from NEMO.models import User
from NEMO_timezone.models import UserPreferencesTimezone
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class UserTimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user: User = request.user
        try:
            tz: str = user.preferences.timezone.timezone
            if tz and isinstance(tz, str):
                timezone.activate(pytz.timezone(tz))
            else:
                timezone.deactivate()
        except (UserPreferencesTimezone.DoesNotExist, AttributeError):
            # we expect this when no preferences exist yet
            pass
