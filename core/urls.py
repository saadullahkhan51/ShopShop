from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

urlpatterns = [
    # /core/
    # path('', views.index, name='index'),
    path('', ProductListView.as_view(), name='index'),
    # /core/product/2/
    # path('product/<int:pk>/', views.detail, name='detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]