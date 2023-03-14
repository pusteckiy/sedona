from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from src.shop.models import Product, PurchaseHistory, Category


def shop_main(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context={
        'products': products,
        'categories': categories,
        }
    if request.user.is_authenticated:
        context.update({
            'money': request.user.money, 
            'nickname': request.user.nickname
        })
    return render(request, 'shop.html', context)


@csrf_exempt
def shop_buy_product(request, product_id: int):
    if request.method == "POST":
        if request.user.is_anonymous:
            return JsonResponse({'status': 'error', 'message': 'Авторизуйтесь для начала.'})
        product = Product.objects.get(id=product_id)
        if product.currency == 'SA$':
            if request.user.money < product.price:
                return JsonResponse({'status': 'error', 'message': 'Недостаточно SA$ на счету.'})
            request.user.money -= product.price

        if product.currency == 'SC':
            if request.user.coins < product.price:
                return JsonResponse({'status': 'error', 'message': 'Недостаточно SC$ на счету.'})
            request.user.coins -= product.price

        purchase = PurchaseHistory(profile=request.user, product=product, price=product.price)
        
        request.user.save()
        purchase.save()
        return JsonResponse({'status': 'ok', 'message': 'Вы успешно приобрели продукт.'})
        