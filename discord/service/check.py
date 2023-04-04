def form_ban(ban):
    if ban:
        return f"Блокировка\n┣ Причина: {ban.get('reason')}\n┣ Админ: {ban.get('admin')}\n┣ Дата: {ban.get('date')}\n┗ Время: {ban.get('time')}"
    return 'Блокировка: -'


def form_cars(cars):
    if cars:
        last_car = cars.pop()
        cars_list = ''.join((f"\n┣ {car[1]} [{car[0]}]" for car in cars))
        return 'Авто' + cars_list + f"\n┗ {last_car[1]} [{last_car[0]}]"
    return 'Авто: -'


def form_list_of_property(property):
    if property:
        return ', '.join(map(str, property))
    return '-'


def form_storage(storage):
    if storage:
        last_storage = storage.pop()
        storage_list = ''.join((f"\n┣ #{row['id']} в складском помещении #{row['warehouse']}" for row in storage))
        return "Склады" + storage_list + f"\n┗ #{last_storage['id']} в складском помещении #{last_storage['warehouse']}"
    return 'Склады: -'


def form_player_stats_answer(player):
    nick = player.get('nick')
    id = player.get('id')
    level = player.get('level')
    vip = player.get('vip')
    phone = player.get('phone')
    money = player.get('money')
    bank = player.get('bank')
    deposit = player.get('deposit')
    bank_1 = player.get('bank1')
    bank_2 = player.get('bank2')
    bank_3 = player.get('bank3')
    euro = player.get('euro')
    btc = player.get('btc')
    donate = player.get('donate')
    family = player.get('family')
    family_id = player.get('familyId')
    fraction = player.get('fraction')
    fraction_id = player.get('fractionId')
    rank_name = player.get('rankName')
    rank = player.get('rank')
    warns = player.get('warns')
    mute_time = player.get('muteTime')
    demorgan_time = player.get('demorganTime')
    ban = player.get('ban')
    cars = player.get('cars')
    houses = player.get('houses')
    bizneses = player.get('bizneses')
    storage = player.get('storage')

    ban = form_ban(ban)
    cars = form_cars(cars)
    houses = form_list_of_property(houses)
    bizneses = form_list_of_property(bizneses)
    storage = form_storage(storage)

    title = f"{nick} [{id}]"
    description = f"**Основное:**\nУровень: {level}\nВип: {vip}\nТелефон: {phone}\nДонат: {donate}\n\n" \
        f"**Вирты:**\nНа руках: {money}\nБанк: {bank}\nДепозит: {deposit}\nДоп.счет #1: {bank_1}\nДоп.счет #2: {bank_2}\nДоп.счет #3: {bank_3}\nЕвро: {euro}\nBTC: {btc}\n\n" \
        f"**Другое**:\nСемья: {family} [{family_id}]\nФракция: {fraction} [{fraction_id}]\nДолжность: {rank_name} [{rank}]\n\n" \
        f"**Наказания:**\nВарны: {warns}\nМут: {mute_time}\nДеморган: {demorgan_time}\n{ban}\n\n" \
        f"**Имущество**:\n{cars}\nДома: {houses}\nБизнесы: {bizneses}\n{storage}"

    return title, description
