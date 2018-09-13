__author__ = 'jim'
__date__ = '16:53,2018/9/13'

from django import forms


class LoginForm(forms.Form):
    # 账号密码都不为空
    username=forms.CharField(required=True)
    password=forms.CharField(required=True,min_length=5)


