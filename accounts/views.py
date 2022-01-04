import requests
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from accounts.forms import SignupForm
from .models import User
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 환영합니다.")
            # signed_user.send_welcome_email()  # FIXME: Celery로 처리하는 것을 추천.
            next_url = request.GET.get('next', '/')
            return redirect('products:list')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

def kakao_signin(request):
    client_id = "56e75c53e4ab061784668dc4787e4fdd"
    REDIRECT_URI = "http://127.0.0.1:8000/accounts/signin/kakao/callback/"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={REDIRECT_URI}&response_type=code"
    )
class KakaoException:
    pass
def kakao_callback(request: HttpRequest):
    # (1)
    code = request.GET.get("code")
    client_id = "56e75c53e4ab061784668dc4787e4fdd"
    REDIRECT_URI = "http://127.0.0.1:8000/accounts/signin/kakao/callback/"

    # (2)
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={REDIRECT_URI}&code={code}"
    )

    # (3)
    token_json = token_request.json()
    error = token_json.get("error", None)
    if error is not None:
        raise KakaoException()
    # (4)
    access_token = token_json.get("access_token")

    # (5)
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    profile_json = profile_request.json()
    properties = profile_json.get("properties")
    kakao_account = profile_json.get("kakao_account")

    name = properties['nickname']
    email = kakao_account['email']
    gender = kakao_account['gender']
    password = profile_json['id']
    user = authenticate(request, username=email)

    if User.objects.get(email=kakao_account['email']) == 'null':
        User.objects.create_user(username=email,name=name,
                                 paswwowrd=password,
                                 email=email, gender=gender)
        login(request, user)
        return redirect('products:list')
    user = authenticate(request, username=email,password=password)
    login(request, user)
    return redirect('products:list')