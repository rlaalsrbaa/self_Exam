import requests
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from accounts.forms import SignupForm
from .models import User

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

def kakao_signin(request: HttpRequest):
    client_id = "b802f6445a425bd9e26623bdc8119bb5"
    REDIRECT_URI = "http://127.0.0.1:8000/accounts/signin/kakao/callback/"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={REDIRECT_URI}&response_type=code"
    )


class KakaoException:
    pass


def kakao_callback(request):
    #(1)
    code = request.GET.get("code")
    client_id = "b802f6445a425bd9e26623bdc8119bb5"
    REDIRECT_URI = "http://127.0.0.1:8000/accounts/signin/kakao/callback/"

    #(2)
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={REDIRECT_URI}&code={code}"
    )
    #(3)
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
    id = profile_json.get("id")
    properties = profile_json.get("properties")

    if properties != None:
        id = properties.get("nickname")
        return HttpResponse(id)
    #User.objects.create_user(username=id)
    return HttpResponse(profile_json.get("properties"))