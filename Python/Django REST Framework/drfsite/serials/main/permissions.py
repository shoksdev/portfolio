from rest_framework import permissions


class MainPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif view.action == 'destroy' or view.action == 'update':
            return request.user == obj.author
        elif view.action == 'destroy':
            return request.user.is_staff
        elif view.action == 'create':
            return request.user.is_authenticated
        else:
            return False
