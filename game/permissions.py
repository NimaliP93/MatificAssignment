from django.contrib.auth.models import User
from rest_framework import permissions


def is_user_in_group(user_id, group):
    return User.objects.filter(pk=user_id, groups__name=group).exists()


def has_group_permission(user, groups):
    return any([is_user_in_group(user, grp) for grp in groups])


class IsAdmin(permissions.BasePermission):
    groups = ['Admin']

    def has_permission(self, request, view):
        return has_group_permission(request.user.id, self.groups)


class IsCoach(permissions.BasePermission):
    groups = ['Coach']

    def has_permission(self, request, view):
        return has_group_permission(request.user.id, self.groups)


class IsAdminOrCoach(permissions.BasePermission):
    groups = ['Admin', 'Coach']

    def has_permission(self, request, view):
        return has_group_permission(request.user.id, self.groups)
