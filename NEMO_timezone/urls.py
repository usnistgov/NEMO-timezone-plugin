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


router.register(r"tools_with_tz", NewToolViewSet)

urlpatterns = [
    path("user_preferences/", views.custom_user_preferences, name="user_preferences")
]
