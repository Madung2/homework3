from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta

class TakesThreeMinutesToWrite(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        # Date field : 2022-06-20
        # DateTime field : 2022-06-20 10:50:00
        print(user.join_date)
        print(datetime.now().date - timedelta(days=3))
        return bool(user.join_date < datetime.now().date() - timedelta(minutes=3)) 
        