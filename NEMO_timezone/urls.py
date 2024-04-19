from NEMO.serializers import ToolSerializer
from NEMO.urls import router
from NEMO.views.api import ToolViewSet
from django.urls import path
from rest_framework import serializers

from NEMO_timezone import views


class NewToolSerializer(ToolSerializer):
    timezone = serializers.CharField(read_only=True, source="timezone.timezone")


class NewToolViewSet(ToolViewSet):
    serializer_class = NewToolSerializer


def replace_api_url(url_to_replace, new_config):
    for reg in router.registry:
        if reg[0] == url_to_replace:
            router.registry.remove(reg)
    router.register(*new_config)


router.register(r"tools_with_tz", NewToolViewSet, basename="tools_with_tz")
replace_api_url("tools", (r"tools", NewToolViewSet))
router.registry.sort(key=lambda x: (x[0].count('/'), x[0]))

urlpatterns = [
    path("user_preferences/", views.custom_user_preferences, name="user_preferences")
]
