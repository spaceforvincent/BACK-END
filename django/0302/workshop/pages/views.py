from django.shortcuts import render
import random

def dinner(request, menu, people):
    context = {
        'menu': menu,
        'people':people,
    }
    return render(request, 'dinner.html', context)


def lotto(request):
    numbers = random.sample(range(1, 46), 6)
    context = {
        'numbers':numbers,
    }
    return render(request, 'lotto.html', context)