from django.conf.urls import url

from users import views

urlpatterns = [
	# 用户注册
	url(r'^register/$',views.register,name='register'),

	# 注册页面表单提交
	url(r'^register_handle/$', views.register_handle, name='register_handle'),

	# 显示登录页面
	url(r'^login/$',views.login,name='login'),

	#用户登录校验
	url(r'^login_check/$',views.login_check,name='login_check'),

# 	用户退出登录
	url(r'^logout/$',views.logout,name='logout')

# 	用户中心-信息页
# 	url(r'^$'.views.use,name='user'),



]
