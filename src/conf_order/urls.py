from django.urls import path
from conf_order.views import CreateOrderView

app_name = 'conf_order'
urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='create_order'),
]