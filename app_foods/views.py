from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime

all_foods = [
    {
        'id': 1, 'title': 'apple', 'price': 599,
        'date': datetime(2023, 4, 23)
    },
    {
        'id': 2, 'title': 'orange', 'price': 789,
        'date': datetime(2023, 4, 23)
    }
]

# Create your views here.


def foods(request):
    context = {'foods': all_foods}
    return render(request, 'app_foods/foods.html', context)


def food(request, food_id):
    one_food = None
    try:
        one_food = [f for f in all_foods if f['id'] == food_id][0]
    except IndexError:
        print('cbcb')
    context = {'food': one_food}
    return render(request, 'app_foods/food.html', context)
