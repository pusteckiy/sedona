import requests
import re
import random

from datetime import datetime, timedelta
from bs4 import BeautifulSoup

from django.conf import settings
from src.api.models import Command

session = requests.Session()
payment_regex = re.compile("(\d+\-\d+-\d+\s\d+\:\d+\:\d+)\sИгрок\s(\w+)\sперевёл\sигроку\sCyberSedona\s([\d|,]+)\s\$\sна\sбанк")


def exchange_code(code: str):
    data = {
        "client_id": "821736713231007765",
        "client_secret": "2RNz8VGWRXcn1NUtRV1uh5AkXn3Ez-OR",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": f"https://{settings.DOMAIN}/redirect",
        "scope": "identify"
        }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    access_token = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers).json()['access_token']
    response = requests.get("https://discord.com/api/v10/users/@me", headers={'Authorization': 'Bearer %s' % access_token})
    return response.json()


def is_logged():
    r = session.get('https://arizonarp.logsparser.info/profile')
    return 'Двухфакторная аутентификация подключена' in r.text


def gp_login(name: str, password: str):
    response = session.get('http://arizonarp.logsparser.info/login')
    soup = BeautifulSoup(response.content, features='html.parser')
    token = soup.find('meta', {'name': 'csrf-token'})['content']
    data = {'name': name, 'password': password, '_token': token}
    response = session.post('https://arizonarp.logsparser.info/login', data=data)
    soup = BeautifulSoup(response.content, features='html.parser')
    token = soup.find('meta', {'name': 'csrf-token'})['content']
    two_f_data = {'_token': token, 'code': 0}
    session.post('https://arizonarp.logsparser.info/authenticator', data=two_f_data)


def search_by_param(param, nickname) -> list:
    log_list = []
    response = session.get(f'https://arizonarp.logsparser.info/?server_number=22&type%5B%5D={param}&sort=desc&player={nickname}')
    soup = BeautifulSoup(response.content, features='html.parser')
    table = soup.find('table', {'class': 'table table-hover'})
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')
    for tr in trs:
        td = tr.find_all('td')
        log = f"{td[0].get_text().strip()} {td[1].get_text().strip()}"
        log_list.append(log)
    return log_list


def check_SAMP_payment(nickname) -> tuple:
    """ Якщо знайшло оплату по вказаному ніку то повертає лог і суму без ком. Якщо ні, то None """
    
    if not is_logged():
        gp_login(settings.GP_LOGIN, settings.GP_PASSWORD)
    
    minus_time = datetime.now(tz=settings.PYTZ_TIME_ZONE) - timedelta(seconds=20)
    log = search_by_param('bank', 'CyberSedona')
    for row in log:
        found_regex = payment_regex.findall(row)
        if len(found_regex) != 0:
            row_date, row_nickname, row_amount = found_regex.pop()
            payment_time = datetime.strptime(row_date, '%Y-%m-%d %H:%M:%S')
            localized_payment_time = settings.PYTZ_TIME_ZONE.localize(payment_time, is_dst=None)
            if row_nickname == nickname and localized_payment_time > minus_time:
                return row, int(row_amount.replace(',', ''))
    return None, None


def send_random_code(nickname):
    """ Записує код для відправки RakBot """
    verification_code = random.randint(100000, 999999)
    Command.objects.create(
        text=f'/pm {nickname} 0 [УВЕДОМЛЕНИЕ] Код для подтверждения аккаунта: {verification_code}', 
        user='RakBot'
        )
    return verification_code
