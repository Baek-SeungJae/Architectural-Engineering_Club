from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import get_user_model
from django.contrib import messages

import requests
import json
from django.db.models import Q

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.views import SignupView


# Create your views here.

def index(request):
    return redirect('accounts:login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('draw:index')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user,
                           backend='django.contrib.auth.backends.ModelBackend')
                Profile.objects.create(user=user)
                messages.success(request, '회원가입 완료')
                return redirect('accounts:index')
            else:
                messages.error(request, '회원가입 실패')
        else:
            form = UserCreationForm()
        context = {
            'form': form
        }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('draw:index')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                messages.success(request, '로그인 완료')
                return redirect(request.GET.get('next') or 'draw:index')
            else:
                messages.error(request, '로그인 실패')
        else:
            form = AuthenticationForm
        context = {
            'form': form
        }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')


def profile(request, username):
    # 회원 프로필보기 화면인데 현재 미구현
    context = {
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def delete(request):
    request.user.delete()
    return redirect('accounts:index')


@login_required
def update(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if profile:
        profile = request.user.profile
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            # p_form = PasswordChangeForm(request.user, request.POST)
            p_form = ProfileForm(request.POST, instance=profile)
            if form.is_valid() and p_form.is_valid():
                p = p_form.save(commit=False)
                p.student_no = request.POST.get('student_no')
                form.save()
                p.save()
                # user = p_form.save()
                # update_session_auth_hash(request, user)
                messages.success(request, '개인정보 수정 완료')
                return redirect('accounts:index')
            else:
                messages.success(request, '개인정보 수정 실패')
        else:

            form = CustomUserChangeForm(instance=request.user)
            p_form = ProfileForm(instance=request.user.profile)
            # p_form = PasswordChangeForm(request.user, request.POST)
    context = {
        'form': form,
        'p_form': p_form
    }
    return render(request, 'accounts/update.html', context)


@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호 변경 완료')
            return redirect('accounts:index')
        else:
            messages.success(request, '비밀번호 변경 실패')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/password.html', context)
