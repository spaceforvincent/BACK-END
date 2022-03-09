from django.shortcuts import render
import random

def index(request):
    return render(request, 'articles/index.html')


def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name': 'Alice'
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'articles/greeting.html', context)


def dinner(request):
    foods = ['카레', '삼겹살', '떡볶이', '김밥', '치킨']
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'articles/dinner.html', context)


def dtl_practice(request):
    foods = ['짜장면', '탕수육', '짬뽕', '양장피']
    fruits = ['apple', 'banana', 'cucumber', 'mango']
    user_list = []
    context = {
        'foods': foods,
        'fruits': fruits,
        'user_list': user_list,
    }
    return render(request, 'articles/dtl_practice.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)