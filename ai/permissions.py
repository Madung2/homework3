from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta

SAFE_METHODS = ('GET')
class TakesThreeMinutesToWrite(BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        # Date field : 2022-06-20
        # DateTime field : 2022-06-20 10:50:00
        print(user.join_date)
        print(datetime.now().date - timedelta(days=1))
        if user.is_authenticated and request.method in SAFE_METHODS:
            return True
        return bool(user.join_date < datetime.now().date() - timedelta(days=1)) 
        


class AdminOrSevenDaysUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool((request.user and request.user.is_staff) or (bool(user.join_date < datetime.now().date() - timedelta(minutes=3))))


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_authenticated
        )
        
        
class ThreeDayUserCanWrite(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        return bool(
            (request.method in SAFE_METHODS) or
            (request.user and datetime.now().date() - user.join_date >= timedelta(days=3))
        )