import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import random
import string


list_address = []
list_img = []
headers = {
"Accept":"*/*",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
"Cache-Control":"no-cache",
"Cookie":
"yabs-sid=519410671683731962; yandexuid=4762841871673366204; yuidss=4762841871673366204; i=6Tu+fISYJx+hiOsArN5qBGsF2pqQ7V9U8d09mLHJ3ltgZWb5LzlFKikFlqG6Rp2BtpReGRQihsy1rhZTmwtnbI6qip4=; ymex=1686388104.oyu.7198215791683731962#1999091962.yrts.1683731962#1999091962.yrtsi.1683731962; gdpr=0; _ym_uid=1673463093485941; _ym_d=1684413912; my=YwA=; yandex_login=ivanovas00; ys=udn.cDppdmFub3ZhczAw#c_chck.2662432188; Session_id=3:1691344999.5.0.1686072490803:u_MSBQ:4b.1.2:1|809930545.0.2.3:1686072490|3:10273881.979379.gQxh1QoyUTxHUzas9pj618v5_t4; sessar=1.827.CiCcSmAm-Mg5XfvmV95GEWMcpVRPoF6dVKO0ok7LADtBqQ.fhvMYqvk_NtydLFXSvzeB_354Xk1zzkESumV_AxuwUc; sessionid2=3:1691344999.5.0.1686072490803:u_MSBQ:4b.1.2:1|809930545.0.2.3:1686072490|3:10273881.979379.fakesign0000000000000000000; instruction=1; yp=2001432490.udn.cDppdmFub3ZhczAw#2001432490.multib.1#1694107731.ygu.1; yandex_gid=2; is_gdpr=1; is_gdpr_b=CMCmehC+xwEYASgC; _ym_isad=1; bh=EkEiTm90L0EpQnJhbmQiO3Y9Ijk5IiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjExNSIsICJDaHJvbWl1bSI7dj0iMTE1IhoFIng4NiIiECIxMTUuMC41NzkwLjE3MSIqAj8wOgkiV2luZG93cyJCCCIxNS4wLjAiSgQiNjQiUlwiTm90L0EpQnJhbmQiO3Y9Ijk5LjAuMC4wIiwiR29vZ2xlIENocm9tZSI7dj0iMTE1LjAuNTc5MC4xNzEiLCJDaHJvbWl1bSI7dj0iMTE1LjAuNTc5MC4xNzEiIg==",
"Origin":"https://street-viewer.ru",
"Pragma":"no-cache",
"Referer":"https://street-viewer.ru/",
"Sec-Ch-Ua":"'Not/A)Brand';v='99', 'Google Chrome';v='115', 'Chromium';v='115'",
"Sec-Ch-Ua-Mobile":"?0",
"Sec-Ch-Ua-Platform":"Windows",
"Sec-Fetch-Dest":"empty",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Site":"cross-site",
"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
response = requests.get(url="https://street-viewer.ru/spb/", headers=headers)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
div_elements = soup.find_all('div', class_='pb-1')
for div in div_elements:
    text = div.get_text(strip=True)
    text_without_ostanovka = text.replace('Остановка', '')
    list_address.append(text_without_ostanovka)

response2 = requests.get(url="https://sisters.spb.ru/portfolio/", headers=headers)
response2.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
div_elements2 = soup.find_all('img', class_='attachment-vp_xl size-vp_xl')
for div in div_elements2:
    text = div.get_text(strip=True)
    text_without_ostanovka = text.replace('Остановка', '')
    list_address.append(text_without_ostanovka)

response2 = requests.get(url="https://sisters.spb.ru/portfolio/", headers=headers)
response2.encoding = "utf-8"
soup = BeautifulSoup(response2.text, "lxml")
div_elements2 = soup.find_all('img', class_='attachment-vp_xl size-vp_xl')
for div in div_elements2:
    src_value = div.get("src")
    list_img.append(src_value)

def generate_random_phone_number():
    rest_of_number = ''.join(random.choice('0123456789') for _ in range(9))
    phone_number = '+7' + rest_of_number
    return phone_number

def generate_random_date(start_date):
    current_date = datetime.now()
    days_difference = (current_date - start_date).days
    random_days = random.randint(0, days_difference)
    random_date = start_date + timedelta(days=random_days)
    return random_date

list_job_tittle = ["Администратор", "Парикмахер-стилист", "Мастер маникюра", "Косметолог", "Визажист", "Массажист",
                   "Работа за процент"]

def generate_random_email(length=8):
    letters = string.ascii_lowercase
    domain = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]  # Вы можете добавить дополнительные домены
    username = ''.join(random.choice(letters) for _ in range(length))
    email = f"{username}@{random.choice(domain)}"
    return email

rasxodnye_materialy = [
    "Шампуни",
    "Кондиционеры",
    "Масла для волос",
    "Лаки для ногтей",
    "Гели для маникюра",
    "Акриловые материалы для ногтей",
    "Косметика для лица",
    "Маски и пилинги",
    "Салфетки и полотенца",
    "Перчатки одноразовые",
    "Маски для лица",
    "Насадки для аппаратов косметологии",
    "Инструменты для маникюра и педикюра",
    "Зажимы и заколки для волос",
    "Подушечки для головы при мойке волос",
    "Бумажные полотенца",
    "Салфетки для дезинфекции",
    "Салфетки для снятия макияжа",
    "Маникюрные и педикюрные пилки",
    "Одноразовые стрижки для лица",
    "Пудра для укладки волос",
    "Одноразовые полотенца для рук",
    "Краски для волос",
    "Кисти и аппликаторы для макияжа",
    "Ватные диски и палочки",
    "Лента и пленка для наращивания ногтей",
    "Дезинфицирующие средства",
    "Упаковочные материалы для товаров",
    "Фольга для мелирования волос",
    "Подушки для массажных столов",
    "Ароматические масла для массажа",
    "Антисептики для рук",
    "Средства для удаления волос",
    "Салфетки для макияжа",
    "Клипсы для укладки волос",
    "Зубные щетки и пасты для клиентов",
    "Одноразовые пончики для маникюра",
    "Мусорные пакеты",
    "Душистые свечи и ароматы",
    "Прокладки и тампоны для женщин",
    "Очки для солярия",
    "Масла для массажа",
    "Очищающие салфетки для лица",
    "Одноразовая одежда для клиентов",
    "Прокладки для глаз при наращивании ногтей",
    "Бигуди и заколки для укладки волос",
    "Дисконтные карты и купоны",
    "Расчески и распылители для волос",
    "Одноразовая посуда для напитков",
    "Салфетки для ухода за очками солярия",
]




akcii_dict = {
    "Летнее освежение": "скидка 20% на все виды маникюра",
    "День релаксации": "массаж спины по цене маникюра",
    "Горячее предложение": "стрижка + укладка за 1000 рублей",
    "Красота в каждом пальце": "скидка на покрытие гелем при маникюре",
    "VIP уход за волосами": "бесплатная маска при укладке",
    "Осенний момент": "скидка на сезонные цветы для волос",
    "Сияние лета": "загар в солярии + подарок косметика для загара",
    "День красоты": "скидка 30% на все услуги салона",
    "Приведи друга и получи скидку на следующий визит": "",
    "Бодрящий массаж": "скидка на антицеллюлитный массаж",
    "Лучшие друзья": "скидка на парное мыло и скраб для друзей",
    "Красота в деталях": "укладка бровей в подарок при покрытии гелем",
    "Свадебная фея": "специальная подготовка невесты",
    "Мужской уход": "скидка на мужскую стрижку и бритье",
    "Творческий образ": "экспериментируй с цветом волос по акции",
    "Гладкие ножки": "скидка на педикюр с покрытием"
}






