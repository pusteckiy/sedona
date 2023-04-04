from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, JsonResponse

from src.account.service import exchange_code, check_SAMP_payment, send_random_code
from src.account.models import Deposit
from src.api.models import Command
from src.shop.models import PurchaseHistory
from src.account.forms import ConnectAccountForm, InputAccountCodeForm, ClearAccountFromRakBotForm
from config.settings import DISCORD_REDIRECT_URL


def account_login(_):
    return redirect(DISCORD_REDIRECT_URL)


def account_login_redirect(request):
    code = request.GET.get('code')
    if not code:
        return redirect('/')
    discord_user = exchange_code(code)
    user = authenticate(request, discord_user=discord_user)
    login(request, user)
    return redirect('/account')


@login_required(login_url='/account/login')
def account_logout(request: HttpRequest):
    logout(request)
    return redirect('/')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@login_required(login_url='/account/login')
def account_main(request: HttpRequest):
    purchase_history = PurchaseHistory.objects.all().filter(profile=request.user)
    deposit_history = Deposit.objects.all().filter(profile=request.user)
    context = {
        'user': request.user,
        'found_ip': get_client_ip(request),
        'deposit_history': deposit_history,
        'purchase_history': purchase_history,
        'connect_account_form': ConnectAccountForm(),
        'input_account_code_form': InputAccountCodeForm(),
        'clear_account_from_rakbot_form': ClearAccountFromRakBotForm(),
    }
    return render(request, 'account.html', context)


@login_required(login_url='/account/login')
def account_connect(request: HttpRequest):
    if request.method == 'GET':
        request.user.is_active = False
        request.user.save()
        return HttpResponse('saved')

    if request.method == 'POST':
        if request.user.is_active:
            return JsonResponse({'status': 'error', 'message': 'Аккаунт уже активирован.'})
        nickname = request.POST.get('nickname')
        verification_code = send_random_code(nickname)
        request.user.nickname = nickname
        request.user.verification_code = verification_code
        request.user.save()
        return JsonResponse({'status': 'ok', 'message': 'Отправлен код активации.'})


@login_required(login_url='/account/login')
def account_connect_code(request: HttpRequest):
    if request.method == 'POST':
        input_code = request.POST.get('code')
        user_code = request.user.verification_code
        if int(input_code) != user_code:
            return JsonResponse({'status': 'error', 'message': 'Неправильный код активации.'})
        request.user.is_active = True
        request.user.save()
        return JsonResponse({'status': 'ok', 'message': 'Аккаунт активирован.'})


@login_required(login_url='/account/login')
def account_deposit(request: HttpRequest):
    if request.method == 'POST':
        nickname = request.user.nickname
        log, amount = check_SAMP_payment(nickname)
        check_deposit = Deposit.objects.filter(string=log)
        if log is None or len(check_deposit) != 0:
            return JsonResponse({
                'status': 'error', 'log': 'Пополнений не найдено!', 'amount': 0,
            })

        deposit = Deposit(profile=request.user, string=log)
        deposit.save()
        request.user.money += amount
        request.user.save()
        return JsonResponse({
            'status': 'ok', 'log': log, 'amount': amount,
        })


@login_required(login_url='/account/login')
def account_clear_rakbot(request: HttpRequest):
    if request.method == 'POST':
        form = ClearAccountFromRakBotForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data['ip']
            Command.objects.create(
                text=f">> clearrakbot {request.user.nickname} {ip}",
                user=request.user.id
            )
            return JsonResponse({'status': 'ok', 'message': 'Отправлено на обработку.'})
        return JsonResponse({'status': 'error', 'message': 'Неправильный запрос.'})

