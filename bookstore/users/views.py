from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
import re
from users.models import Passport
from django.http import JsonResponse

from users.models import Address
from utils.decorators import login_required
# from django. import Address


# Create your views here.

@login_required
def user(request):
    passport_id = request.session.get('passport_id')
    addr = Address.objects.get_default_address(passport_id=passport_id)

    books_li = []

    context = {
        'addr':addr,
        'page':'user',
        'books_li':books_li
    }

    return render(request,'users/user_center_info.html',context)




def logout(request):
    request.session.flush()
    return redirect(reverse('books:index'))


def login_check(request):
    # 用户登录校验
    # 获取数据
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    print(username)
    print(password)
#     数据校验
    if not all([username,password]):
        print('222')
        return JsonResponse({'res':2})
    print('5555')
    passport = Passport.objects.get_one_passport(username=username,password=password)
    print(passport)
    if passport:
        print('3333')
        next_url = request.session.get('url_path',reverse('books:index'))
        jres = JsonResponse({'res':1,'next_url':next_url})

        if remember == 'true':
            jres.set_cookie('username',username,max_age=7*24*3600)

        else:
            jres.delete_cookie('username')

        request.session['islogin'] = True
        request.session['username'] = username
        request.session['passport_id'] = passport.id
        return jres

    else:
        return JsonResponse({'res':0})

def login(request):
    # 显示登录页面
    username = ''
    checked = ''

    context = {
        'username':username,
        'checked':checked,
    }

    return render(request,'users/login.html',context)



def register(request):
    # 显示用户注册页面
    return render(request, 'users/register.html')


def register_handle(request):
    # 进行用户注册处理
    # 接收数据
	# 用户名
    username = request.POST.get('user_name')
    # 密码
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    print(username)
    print(password)
    print(email)
    # 进行数据校验
    if not all([username, password, email]):
        print('mmm')
        # 有数据为空
        return render(request, 'users/register.html', {'errmsg':'参数不能为空!'})

    # 判断邮箱是否合法
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        print('hhh')
        # 邮箱不合法
        return render(request, 'users/register.html', {'errmsg':'邮箱不合法!'})
    print('bbbb')
    # 进行业务处理:注册，向账户系统中添加账户
    passport = Passport.objects.add_one_passport(username=username, password=password, email=email)
    print(passport)
    # 注册完，还是返回注册页。
    # return redirect(reverse('user:register'))

    return redirect(reverse('books:index'))
