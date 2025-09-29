# views.py
from django.shortcuts import render
from .models import MyInfo,Data,Mark # если решили использовать модель

def contacts(request):
    # Получаем объект контактной информации из базы данных
    try:
        info = MyInfo.objects.first()  # получаем первую запись из таблицы
    except MyInfo.DoesNotExist:
        info = None  # или можно задать дефолтные данные, если записей нет

    # Передаем данные в шаблон
    return render(request, 'index.html', {'info': info})
def user(request):
    ser=Data.objects.first()
    return render(request, 'index.html', {'ser': ser})
def mark(request):
    nn=Mark.objects.all()
  
    context = {
        'nn': nn,
        
    }
    return render(request, 'main.html', context)