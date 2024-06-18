try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

from NEMO.models import User
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from NEMO_timezone.models import UserPreferencesTimezone


class UserTimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user: User = request.user
        try:
            tz: str = user.preferences.timezone.timezone
            if tz and isinstance(tz, str):
                timezone.activate(zoneinfo.ZoneInfo(tz))
            else:
                timezone.deactivate()
        except (UserPreferencesTimezone.DoesNotExist, AttributeError):
            # we expect this when no preferences exist yet
            pass
