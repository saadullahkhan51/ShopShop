from django.urls import path
from . import views

urlpatterns = [
    # /core/
    path('', views.index, name='index'),
    # /core/2/
    path('<int:prodId>/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]