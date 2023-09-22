from django.db import models

from users.models import CustomUser


# Модель Товара с тремя обязательными полями(название, описание, цена)
class Product(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название товара')
    desc = models.TextField(verbose_name='Описание товара')
    price = models.FloatField(default=0, verbose_name='Цена товара')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


# Модель Корзины с двумя обязательными полями(когда была создана и кто владелец)
class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания корзины')
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Владелец корзины')

    def __str__(self):
        return str(self.id)


# Модель Товаров в Корзине с тремя обязательными полями(в какой корзине лежат товары, какие товары и в каком количестве)
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartitems', verbose_name='Товар')
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Владелец элемента корзины')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество товара')


# Модель Заказа с тремя обязательными полями(когда была создана, какой статус заказа и чей это заказ)
class Order(models.Model):
    STATUS_CHOICES = [
        ('О', 'Оплачен'),
        ('З', 'Завершен'),
        ('П', 'Провален')
    ]

    placed = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время оформления')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус заказа')
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Владелец')

    def __str__(self):
        return self.status


# Модель Товаров в Заказе с тремя обязательными полями(что за заказ, какие товары и в каком количестве)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return self.product.title
