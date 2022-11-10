
from .models import Product, Cart, Order
from .serializers import ProductSerializer, UserSerializer, CartSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


# {"username":"user3","email":"user3@gmail.com","password":"12345678","first_name":"user3","last_name":"user3" }
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# {"username":"user3","password":"12345678"}
@api_view(['POST'])
def login_user(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response(request.data, status=status.HTTP_201_CREATED)
    return Response("username or password are incorrect")


@api_view(['Get'])
def logout_user(request):
    logout(request)
    return(Response('You are logged out'))


@ api_view(['GET', 'POST'])
def get_products(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@ api_view(['GET'])
def get_products_by_name(request, name):
    queryset = Product.objects.filter(name__contains=name)
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


# {"pid": "1", "quantity": "1"}
@ api_view(['GET', 'POST'])
def add_to_cart(request):
    try:
        session = Session.objects.get()
        session_data = session.get_decoded()
        user_id = session_data['_auth_user_id']
    except:
        return Response('Please login')
    if request.method == 'GET':
        queryset = Cart.objects.filter(user_id=user_id)
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        product = Product.objects.filter(pk=request.data['pid']).exists()
        if product is False:
            return Response('Product not found')
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            try:
                cart = Cart.objects.get(
                    user_id=user_id,
                    product_id=request.data['pid'])
                cart.quantity += int(request.data['quantity'])
                cart.save()
            except:
                cart = Cart.objects.create(
                    user_id=user_id, quantity=1, product_id=request.data['pid'])
                cart.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET', 'POST'])
def orders(request):
    try:
        session = Session.objects.get()
        session_data = session.get_decoded()
        user_id = session_data['_auth_user_id']
    except:
        return Response('Please login')
    if request.method == 'GET':
        queryset = Order.objects.filter(user_id=user_id)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        cart = Cart.objects.filter(user_id=user_id).exists()
        if cart is False:
            return Response('Your cart is Empty')
        cart_items = Cart.objects.filter(user_id=user_id)
        # user = User.objects.get(pk=user_id)
        # order = Order.objects.create(user=user)
        order_items = [
            Order(
                user_id=user_id,
                product=item.product,
                quantity=item.quantity

            ) for item in cart_items
        ]
        Order.objects.bulk_create(order_items)
        Cart.objects.filter(user_id=user_id).delete()
        return Response('Your order is placed')
