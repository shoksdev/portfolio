from django.contrib import admin  # Импортируем функционал для работы с админ-панелью

from .models import Product, Cart, CartItems, OrderItem, Order  # Импортируем модели


# Регистрируем в админ-панели модель Товара
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


# Регистрируем в админ-панели модель Корзины
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'created')


# Регистрируем в админ-панели модель Товаров в Корзине
@admin.register(CartItems)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')


# Регистрируем в админ-панели модель Заказа
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('placed', 'status', 'owner')


# Регистрируем в админ-панели модель Товаров в Заказе
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
