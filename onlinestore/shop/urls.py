from django.urls import path
from .views import GetTokenView, GoodsListView, NewGoodView

urlpatterns = [
    path('get_token/', GetTokenView.as_view(), name='get_token'),
    path('goods/', GoodsListView.as_view(), name='goods_list'),
    path('new_good/', NewGoodView.as_view(), name='new_good'),
]