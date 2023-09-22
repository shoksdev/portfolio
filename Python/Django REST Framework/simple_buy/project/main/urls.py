from django.urls import path, include
from rest_framework_nested import routers

from .views import ProductViewSet, CartViewSet, CartItemViewSet, OrderViewSet  # Импортируем вьюсеты

app_name = 'main'  # Даём Django понять что это за приложение

router = routers.SimpleRouter()  # Создаем роутер для вьюсетов
router.register(r'products', ProductViewSet)  # Регистрируем вьюсет, отвечающий за продукты
router.register(r'carts', CartViewSet)  # Регистрируем вьюсет, отвечающий за корзину
router.register(r'orders', OrderViewSet, basename='orders')  # Регистрируем вьюсет, отвечающий за заказ

# Создаём вложенный роутер из библиотеки drf-nested-routers для вывода товаров корзине и добавления к ним новых
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet,
                     basename='cart-items')  # Регистрируем вьюсет, отвечающий за товары в корзине

urlpatterns = [
    path('', include(router.urls)),  # Включаем пути из роутера
    path('', include(cart_router.urls))  # Включаем пути из вложенного роутера
]
