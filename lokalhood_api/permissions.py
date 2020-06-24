from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """ check if user is trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id


class UpdateOwnRequest(permissions.BasePermission):
    """ Allow users to edit their own request"""

    def has_object_permission(self, request, view, obj):
        """ check if user is trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id==request.user.id
