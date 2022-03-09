from django.shortcuts import render
import random
import requests


def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
    
    # 1. 1회차 당첨 번호 정보 받아오기
    response = requests.get(url)
    lotto = response.json()
    
    # 2. 번호 6개와 보너스 번호 가져오기
    winner = []
    bonus = lotto['bnusNo']
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])
    
    # 3. 당첨 횟수 기록하기 위한 dict 만들기
    win_rate = {'1등': 0, '2등': 0, '3등' : 0, '4등' : 0, '5등': 0, '꽝': 0}

    # 4. 로또 1000장 구매하고 각 당첨번호와 비교하기
    for i in range(1000):
        my_numbers = random.sample(range(1, 46), 6)
        # 4-1. 당첨번호와 자동번호 개수 비교
        cnt = 0
        for num in my_numbers:
            if num in winner:
            # for win in winner:
            #     if num == win:
                    cnt += 1
        # 4-2. 당첨된 횟수 체크
        if cnt == 6:
            win_rate['1등'] += 1
        elif cnt == 5 and bonus in my_numbers:
            win_rate['2등'] += 1
        elif cnt == 5:
            win_rate['3등'] += 1
        elif cnt == 4:
            win_rate['4등'] += 1
        elif cnt == 3:
            win_rate['5등'] += 1
        else:
            win_rate['꽝'] += 1

    # 5. context 만들기
    context = {
        'winner': winner,
        'bonus': bonus,
        'win_rate': win_rate,

    }
    return render(request, 'pages/lotto.html', context)