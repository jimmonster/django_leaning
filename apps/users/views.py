from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from  django.contrib.auth.hashers import make_password

from .models import UserProfile
from .forms import LoginForm,RegisterForm
from utils.email_send import send_register_eamil


# Create your views here.

# 多种数据登录
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 注册

class RegisterView(View):
    def get(self, request):
        register_form=RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})
    def post(self,request):
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')
            # 邮箱验证码
            user_profile=UserProfile()
            user_profile.username=user_name
            user_profile.email=user_name
            user_profile.is_active=False
            user_profile.password=make_password(pass_word)
            # 保存到数据库
            user_profile.save()
            # 发送邮件到邮箱
            send_register_eamil(user_name,'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html',{'register_form':register_form})




# 基于类来定义登录逻辑
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        # loginform是否错误
        if login_form.is_valid():
            # 获取到前端传过来的数据
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')

            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # django 登录api，
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户名或者密码错误！'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


def user_login(request):
    if request.method == 'POST':
        # 获取到前端传过来的数据
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')

        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或者密码错误！'})

    elif request.method == 'GET':
        return render(request, 'login.html', {})
