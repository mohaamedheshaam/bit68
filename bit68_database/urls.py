from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register('products', views.ProductViewSet)
# router.register('add_to_cart', views.AddToCart)
# urlpatterns = router.urls

urlpatterns = [
    path('products/', views.get_products),
    path('products/<str:name>', views.get_products_by_name),
    path('register/', views.register),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('cart/', views.add_to_cart),
    path('order/', views.orders),
]
