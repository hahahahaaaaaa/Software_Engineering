import time
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from .client.Client import *
import json


class User:
    def __init__(self):
        self.flag=False
        self.userName=''

u=User()
#login/register

def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # 处理表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            l = Login(username, password)
            time.sleep(1.2) #等mqtt验证完成 大约要0.2s以上,还有程序运行时间，测试可得时间需要0.8秒
            if l.flag:
                # 登录成功
                u.flag=True #表示登入成功
                u.userName=username
                return redirect('chat')  # 进入'chat'的路由
            else:
                # 登录失败
                messages.error(request, '用户名或密码错误')
                return redirect('login')
    else:
        form = UserForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # 处理表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            print(username)
            print(password)
            if password == confirm_password:
                r = Register(username, password)
                time.sleep(1.2)
                if r.flag:
                    # 注册成功
                    messages.error(request, '注册成功')
                    return redirect('login')
                else:
                    # 注册失败
                    messages.error(request, '注册失败，用户名已存在')
                    return redirect('login')
            else:
                messages.error(request, '两次密码不匹配，请重新输入')
                return redirect('register')  # Redirect to refresh the form
    else:
        form = UserForm()

    return render(request, 'login.html', {'form': form})


#chat
def chat(request):
    username = u.userName
    if username:
        messages.info(request, f"欢迎回来 {username} (●’◡’●)")
    return render(request, 'chat.html')




def getchats(request):
    g=GetMessage(u.userName)
    time.sleep(2)
    comments = g.messages
    if comments:
        for comment in comments:
            comment['time'] = comment['time'].strftime('%Y-%m-%d %H:%M:%S')
        return JsonResponse(comments, safe=False)
    else:
        print("没有评论")

def sendchat(request):
    if request.method == 'POST':
        if u.flag==False:
            return JsonResponse({'status': 'failed', 'message': '未登入，无法评论，请先登入'})
        data = json.loads(request.body)
        message = data.get('message')
        print(message)
        userName=u.userName
        print("u.userName:"+u.userName)
        SendMessage(userName,message)
        time.sleep(2)
        return JsonResponse({'status': 'success','message': '发送成功'})
    return JsonResponse({'status': 'failed'})

def setquestion(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question')
        answer = data.get('answer')
        userName=u.userName
        print("u.userName:"+u.userName)
        print(question)
        print(answer)
        SecurityQuestion(u.userName,question=question,answer=answer)
        time.sleep(2)
        return JsonResponse({'status': 'success','message': '密保设置成功'})
    return JsonResponse({'status': 'failed'})

from .forms import ForgetPasswordForm

def forgetpassword(request):
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']
            password = form.cleaned_data['password']

            s=SecurityQuestion(userName=username,question=question,answer=answer,new_password=password)
            time.sleep(2)
            if s.flag:
                messages.error(request, '密码重置成功')
                return redirect('login')
            else:
                messages.error(request, '用户名或密保错误或未设置密保，请重试')
                return redirect('forgetpassword')


    else:
        form = ForgetPasswordForm()

    return render(request, 'forgetpassword.html', {'form': form})