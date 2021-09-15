from datetime import datetime, timezone

from django.contrib.auth.backends import BaseBackend

from .models import UserActivitySummary


def logUserActivity(request):
    login = '/api-auth/login/'

    if not request.user.is_anonymous:
        if login in str(request.path):
            activity = 'login'
        else:
            activity = 'activity'

        user_last_activity = UserActivitySummary.objects.all().filter(user=request.user).order_by('timestamp').last()

        now = datetime.now(timezone.utc)
        duration = 0
        if user_last_activity:
            duration = (now - user_last_activity.timestamp).seconds

        activity = UserActivitySummary.objects.create(
                                                    user=request.user,
                                                    time_duration=duration,
                                                    activity=activity)
        activity.save()


class LogUserActivityMiddleware(BaseBackend):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logUserActivity(request)
        return self.get_response(request)
