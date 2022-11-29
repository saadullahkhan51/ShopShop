from django.urls import path
from . import views

urlpatterns = [
    # /core/
    path('', views.index, name='index'),
    # /core/2/
    path('<int:prod_id>/', views.show, name='show'),
]