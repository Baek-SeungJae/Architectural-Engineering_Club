from django.shortcuts import render, redirect
from accounts.models import Profile
from .forms import DrawForm
from .forms import Draw
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    user = request.user
    # 소셜로그인과 일반로그인 사이에서 발생하는 오류 처리를 위한 프로필생성
    if len(Profile.objects.filter(user=user)) == 0:
        Profile.objects.create(user=user)
        return redirect('accounts:update')

    # 이미 설문에 응답했을 경우 already=1
    already = 0
    if len(Draw.objects.filter(user=Profile.objects.get(user=user))):
        already = 1

    context = {
        "already": already,
        "name": user.username,
        "student_no": user.profile.student_no,
    }
    return render(request, 'draw/index.html', context)


@login_required
def choose_club(request):
    if request.method == "POST":
        user = Profile.objects.get(user=request.user).user
        user.username = request.POST.get("id")
        user.save()
        name = user.username

        profile = Profile.objects.get(user=request.user)
        profile.student_no = request.POST.get("student_number")
        profile.save()
        student_no = profile.student_no
    else:
        user = Profile.objects.get(user=request.user).user
        name = user.username
        profile = Profile.objects.get(user=request.user)
        student_no = profile.student_no
    form = DrawForm(instance=request.user.profile)
    context = {
        'form': form,
        'name': name,
        'student_no': student_no,
    }
    return render(request, 'draw/club.html', context)


@login_required
def select_finish(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        second = request.POST.get('second')
        third = request.POST.get('third')
        if first != '비작업실':
            if first == second or first == third:
                return redirect('draw:choose_club')
        if second != '비작업실':
            if second == first or second == third:
                return redirect('draw:choose_club')
        if third != '비작업실':
            if third == first or third == second:
                return redirect('draw:choose_club')

        # 학생회장의 긴급요청으로 비작업실 중복선택 가능하게함
        # if first==second or second==third or first==third:

        user = Profile.objects.get(student_no=request.POST.get('student_no'))
        if len(Draw.objects.filter(user=user)) == 0:
            Draw.objects.create(user=user, first=request.POST.get(
                'first'), second=request.POST.get('second'), third=request.POST.get('third'))
        else:
            draw = Draw.objects.get(user=user)
            draw.first = request.POST.get('first')
            draw.second = request.POST.get('second')
            draw.third = request.POST.get('third')
            draw.save()
        context = {
            'first':first,
            'second':second,
            'third':third,
        }
    return render(request, 'draw/finish.html',context)
