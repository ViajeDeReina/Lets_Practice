import requests
from bs4 import BeautifulSoup
import random as rand

menu = ["시원한 육전막국수", "가볍게 서브웨이", "클린한 초밥정식", "육회비빔밥", "아마미 카레돈가스", \
       "연탄불백 정식", "뜨끈한 돼지국밥", "따뜻한 닭칼국수", "개운한 바지락칼국수",\
        "단백질 파우더", "굶는 건", "편의점 샐러드", "*밥천국 '그' 면", "KSA 선정식당", "지하철역 빵 맛집의 빵"]

def crawl():
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EA%B8%88%EC%B2%9C%EA%B5%AC%20%EB%82%A0%EC%94%A8"
    response = requests.get(url, verify = False)
    soup = BeautifulSoup(response.text, 'html.parser')
    NowTemp = soup.find('span', {'class': 'todaytemp'}).text + soup.find('span', {'class' : 'tempmark'}).text[2:]
    return NowTemp

def choose_mode(NowTemp, menu):
    choice_again = True
    while choice_again == True:
        print("1) 보더콜리가 골라주는 메뉴를 먹어볼래.")
        print("2) 랜덤 모드에 도전!")
        selec = int(input("원하는 모드를 선택해줘."))
        if selec == 1:
            print("보더콜리는 무엇을 추천해줄까?")  # it depends on the weather
            choose_menu(NowTemp, menu)
            again = input("다시 고를까? (Y/N)")
            if (again == "Y") | (again == "y"):
                choice_again = True
            else:
                choice_again = False
        elif selec == 2:
            print("무슨 메뉴가 나올지는 보더콜리도 보장할 수 없어.")  # it just chooses anything randomly
            random_choice(menu)
            again = input("다시 고를까? (Y/N)")
            if (again == "Y") | (again == "y"):
                choice_again = True
            else:
                choice_again = False
        else:
            print("1, 2 중에서 선택하는거야. 다시 눌러줘.")
            choice_again = True

def random_choice(menu):
    choice = menu[rand.randint(0,len(menu)-1)]
    print("랜덤 선택의 결과는....")
    print(choice + " 어때?")

def choose_menu(NowTemp, menu):
    # NowTemp from the crawled data, menu as list
    NowTemp = int(NowTemp[:-1])
    if NowTemp >=28:
        choice = menu[rand.randint(0,5)]
    else:
        choice = menu[rand.randint(5,9)]
    print("브로콜리가 고른 오늘의 메뉴는...")
    print(choice + " 어때?")