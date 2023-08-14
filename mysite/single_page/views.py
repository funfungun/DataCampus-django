from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from .models import DataEngCsv
from .serializers import TestDataSerializer
from django.http import JsonResponse
from .forms import AvgCostForm
from django.contrib.sessions.models import Session

def index(request):
    return render(
        request,
        'single_page/index.html'
    )

def first(request):
    return render(
        request,
        'single_page/autonomous.html'
    )

def autonomous(request):
    ms = ['마포구', '서대문구', '종로구']
    latest_list = []

    if request.method == 'POST':
        selected_location = request.POST.getlist('selected_location')

        for location in selected_location:
            if location == '마포구':
                latest_list.extend(DataEngCsv.objects.filter(place_code=0))
            elif location == '서대문구':
                latest_list.extend(DataEngCsv.objects.filter(place_code=1))
            elif location == '종로구':
                latest_list.extend(DataEngCsv.objects.filter(place_code=2))
            elif location == '마포구'and location == '서대문구' :
                latest_list.extend(DataEngCsv.objects.filter(place_code=[0,1]))
            elif location == '마포구'and location == '종로구' :
                latest_list.extend(DataEngCsv.objects.filter(place_code=[0,2]))
            elif location == '서대문구'and location == '종로구' :
                latest_list.extend(DataEngCsv.objects.filter(place_code=[1,2]))
            elif location == '마포구' and location == '서대문구'and location == '종로구' :
                latest_list.extend(DataEngCsv.objects.filter(place_code=[0,1,2]))

        # num = len(latest_list)
        print(latest_list)
        # request.session['latest_list'] = latest_list
        return render(request, "single_page/price.html", {'latest_list': latest_list, 'num' : num})

    else:
        print("POST 요청이 아님")
    
def price(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    j = 0
    if type(title) == str and type(content) == str:
        mon = int(title)
        monf = int(content)
        r = 0.052  # 전월세변환율(5.2%)
        j = mon + (monf * 12 / r)
        print(j)
    filtered_one = DataEngCsv.objects.filter(avg_cost__lte = j)
    print(filtered_one)
    #max_avg_fee = j
    
    return render(request, 'single_page/category.html', )

def category(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items')
        print("선택된 항목:", selected_items)

        # DataEngCsv 모델에서 selected_items에 해당하는 모든 컬럼이 1 이상인 데이터를 추출
        filtered_data = DataEngCsv.objects.filter(**{f"{item}__gte": 1 for item in selected_items})
            
        latest_list = request.session.get('latest_list', [])
        filtered_data = [item for item in filtered_data if item in latest_list]

        return render(request, 'single_page/qq.html', {'filtered_data': filtered_data})

    else:
        print("POST 요청이 아님")
        return render(request, 'single_page/qq.html')
    
def qq(request):
    return render(
        request,
        'single_page/qq.html'
    )

