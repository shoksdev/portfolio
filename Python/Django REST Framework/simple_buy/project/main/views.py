# Импортируем стандартные разрешения, вьюсеты и миксины
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Product, Cart, CartItems, Order  # Импортируем модели
from .serializers import ProductSerializer, CartSerializer, AddCartItemSerializer, CartItemSerializer, \
    UpdateCartItemSerializer, OrderSerializer, CreateOrderSerializer  # Импортируем сериализаторы
from .pagination import ProductPagination  # Импортируем кастомную пагинацию
from .permissions import ProductPermission, CartPermission  # Импортируем кастомные разрешения


# Вьюсет, отвечающий за вывод продуктов с кастомной пагинацией и разрешениями
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (ProductPermission,)
    pagination_class = ProductPagination


# Вьюсет, отвечающий за вывод корзины клиента
class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


# Вьюсет, отвечающий за вывод товаров из корзины клиента на отдельной странице
class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = (CartPermission,)
    http_method_names = ['get', 'post', 'patch', 'delete']  # Обрабатываем только GET, POST, PATCH и DELETE запросы

    def get_queryset(self):
        return CartItems.objects.filter(cart_id=self.kwargs['cart_pk'])  # Находим товары определенной корзины

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer  # Если пользователя отправляет POST запрос - добавляем товар в корзину
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer  # Если пользователя отправляет PATCH запрос - изменяем товар в корзину

        return CartItemSerializer  # Если пользователя отправляет GET запрос - выводим все товары в корзине

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk'], 'user': self.request.user}  # Передаём id корзины в сериализатор



# Вьюсет, отвечающий за заказы, доступен только клиентам
class OrderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'POST':  # Если пользователя отправляет POST запрос - добавляем товар в заказ
            return CreateOrderSerializer

        return OrderSerializer  # Если пользователя отправляет GET запрос - выводим все товары в заказе

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()  # Если пользователь администратор - выводим все заказы
        return Order.objects.filter(owner=user)  # Если пользователь не администратор - выводим только его заказы

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}  # Передаём id пользователя в сериализатор
