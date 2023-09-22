from rest_framework import permissions


# Кастомные разрешения для взаимодействия с товарами(создавать/удалять/изменять может только админ, смотреть - все)
class ProductPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif view.action == 'destroy' or view.action == 'update' or view.action == 'create':
            return request.user.is_staff
        else:
            return False


# Разрешаем взаимодействовать с корзиной только ее владельцу
class CartPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
