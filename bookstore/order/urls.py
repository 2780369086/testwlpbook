from django.conf.urls import url
from order import views

urlpatterns = [
# 	 提交订单页面
	url(r'^place/$',views.order_place,name='place'),

# 	生成订单
	url(r'^commit/$',views.order_commit,name='commit'),
]