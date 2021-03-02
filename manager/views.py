from django.shortcuts import render, redirect
from accounts.models import Profile
from draw.models import Draw
from django.contrib.auth.decorators import login_required
from manager.service.Club_Select_Algorithm import Club_Select_Algorithm
import csv
# Create your views here.

result = dict()

@login_required
def index(request):
    if request.user.is_staff:
        draw = Draw.objects.all()
        context = {
            'draw': draw,
        }

        return render(request, 'manager/index.html', context)
    else:
        return redirect('accounts:index')


def draw_result(request):
    draw = Draw.objects.all()
    
    csvfile = open(file="static/csv/result.csv",
                   mode="w", newline="", encoding="CP949")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['이름', '학번', '1지망', '2지망', '3지망'])
    for data in draw:
        data_to_list = [(data.user.user.username), (data.user.student_no),
                        (data.first), (data.second), (data.third)]
        csvwriter.writerow(data_to_list)
    csvfile.close()
    
    try:
        result = Club_Select_Algorithm().run(request.POST.get('i'))
        context = {
            'result': result,
        }
        return render(request, 'manager/result.html', context)
    except:
        return redirect('manager:index')

    
