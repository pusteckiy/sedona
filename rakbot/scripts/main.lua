require('addon')

local sampev = require('samp.events')
local encoding = require('encoding')
local config = require('config')
local API = require('services.API')
local discord = require('services.discord')

local bankTransfer = {}
local checkoff = {}
local rakBotClearQueue = {}
local lastRakBotIp = ''
local rakBotIp = ''

function onConnect()
    discord.send('**[A]** RakBot connected to the server.')
    API.serverConnect(true)
end

function onDisconnect()
    discord.send('**[A]** RakBot disconnected from the server.')
    API.serverConnect(false)
    config.account.isAuth = false
    clearTasks()
end

function sampev.onShowDialog(id, style, title, btn1, btn2, text)
    -- Account login
    if id == 2 then
        sendDialogResponse(id, 1, -1, config.account.password)
        config.account.id = getBotId()
        config.account.nick = getBotNick()
        newTask(sendInput, 1000, '/az')
        return false
    end

    -- Admin login
    if id == 211 then
        sendDialogResponse(id, 1, -1, config.account.admpass)
        config.account.isAuth = true
        discord.send('**[A]** Logged as ' .. config.account.nick .. ' [' .. config.account.id .. '].')
        newTask(polling)
        return false
    end

    -- Unban accept
    if id == 91 then
        sendDialogResponse(id, 1, -1, 'ok')
        return false
    end

    -- Bank login
    if id == 991 then
        sendDialogResponse(991, 1, -1, config.account.bankpass)
        sleep(1000)
        sendInput('/abankmenu')
        return false
    end

    -- Description
    if id == 15040 then

    end

    -- Stats
    if id == 235 then
        az = text:match('(%d+) az coins')
        moneyInHand = text:match('Наличные деньги %(SA$%): %{B83434%}%[$(%d+)]')
        moneyInBank = text:match('Деньги в банке: {B83434}%[%$(%d+)%]')
        discord.send('**[INFO]**\nAZ: ' .. az .. '\nНаличные: ' .. moneyInHand .. '\nБанк: ' .. moneyInBank)
    end

    if id == 0 then
        checkoff.id = tonumber(text:match('ID в базе данных: (%d+)'))
        checkoff.nick = text:match('Ник: ([%w_]+)')
        checkoff.level = tonumber(text:match('Уровень: (%d+)'))
        checkoff.donate = tonumber(text:match('Донат счет: (%d+)'))
        checkoff.money = tonumber(text:match('Деньги: (%d+)'))
        checkoff.phone = tonumber(text:match('Номер телефона: (%d+)'))
        checkoff.bank = tonumber(text:match('Деньги в банке: (%d+)'))
        checkoff.bank1 = tonumber(text:match('Состояния личного счета №1: ([-%d]+)'))
        checkoff.bank2 = tonumber(text:match('Состояния личного счета №2: ([-%d]+)'))
        checkoff.bank3 = tonumber(text:match('Состояния личного счета №3: ([-%d]+)'))
        checkoff.deposit = tonumber(text:match('Деньги на депозите: (%d+)'))
        checkoff.fraction = u8:encode(text:match('Организация: ([а-яА-Я%w ]+)'))
        checkoff.fractionId = tonumber(text:match('Организация: [а-яА-Я%w ]+ %(№ (%d+)%)'))
        checkoff.rankName = u8:encode(text:match('Должность: ([а-яА-Я%w ]+)'))
        checkoff.rank = tonumber(text:match('Должность: [а-яА-Я%w ]+ %(№ (%d+)%)'))
        checkoff.family = u8:encode(text:match('Семья: ([а-яА-Я%w]+)'))
        checkoff.familyId = tonumber(text:match('FamID: (%d+)'))
        checkoff.warns = tonumber(text:match('Предупреждения: (%d+)'))
        checkoff.vip = u8:encode(text:match('Статус VIP: ([а-яА-Я%w ]+)'))
        checkoff.muteTime = text:match('MuteTime: ([%d:]+)')
        checkoff.demorganTime = text:match('Demorgan: ([%d:]+)')
        checkoff.houses = {}
        if not text:find('Дома:\nОтсутствуют') then
            local temp = text:match("Дома:\n([ID %d+\n]+)")
            for house_id in temp:gmatch('%d+') do
                table.insert(checkoff.houses, tonumber(house_id))
            end
        end
        checkoff.bizneses = {}
        if not text:find('Бизнесы:\nОтсутствуют') then
            checkoff.bizneses = {}
            local temp = text:match("Бизнесы:\n([ID %d+ (%d)\n]+)")
            for biznes_id in temp:gmatch('ID (%d+)') do
                table.insert(checkoff.bizneses, tonumber(biznes_id))
            end
        end
        checkoff.cars = {}
        if not text:find('Автомобили:\nОтсутствуют') then
            local temp = text:match("Автомобили:\n([%[%d+%] %w%WА-Яа-яы]+)\n\n")
            for line in temp:gmatch('[^\n]+') do
                local carId, carName = line:match('%[(%d+)%] ([%wа-яА-Яы ]+)')
                table.insert(checkoff.cars, {tonumber(carId), carName})
            end
        end
        checkoff.storage = {}
        if not text:find('Складская недвижимость: Отсутствуют') then
            local temp = text:match(
                "Складская недвижимость: \n([Склад №%d в складском помещении №%d\n]+)")
            for line in temp:gmatch('[^\n]+') do
                local storageId, warehouse = line:match(
                    'Склад №(%d+) в складском помещении №(%d+)')
                table.insert(checkoff.storage, {
                    ['id'] = tonumber(storageId),
                    ['warehouse'] = tonumber(warehouse)
                })
            end
        end
    end
end

function sampev.onServerMessage(color, text)
    if text:find('[Информация] Вы перевели $%d+ игроку [%w_]+%(%d+%) на счет') then
        bankTransfer.amount, bankTransfer.player, bankTransfer.playerId = text:match(
            '[Информация] Вы перевели $(%d+) игроку ([%w_]+)%(%(d+)%) на счет')
    end
    if text:find(' | Вконтакте: ') then
        checkoff.VK = text:match('| Вконтакте: ([%(%)%w%:а-яА-Я)])')
    end
    if text:find(' | Euro: ') then
        checkoff.euro = tonumber(text:match(' | Euro: (%d+)'))
    end
    if text:find(' | BTC: ') then
        checkoff.btc = tonumber(text:match(' | BTC: (%d+)'))
    end
    if text:find(' | Аккаунт не заблокирован') then
        checkoff.ban = {}
    end
    if text:find(' | Аккаунт заблокирован') then
        local admin, date, time = text:match(
            ' | Аккаунт заблокирован ([%w_]+) админом ([%d-]+) ([:%d]+)')
        checkoff.ban = {
            ['admin'] = admin,
            ['date'] = date,
            ['time'] = time
        }
    end
    if text:find(' | Причина блокировки:') then
        checkoff.ban.reason = u8:encode(text:match(' | Причина блокировки: (.+)'))
    end

    if text:find('Nick %[[%w%W_]+%]  R%-IP %[%d+.%d+.%d+.%d+%]  IP | A%-IP %[{%w+}%d+.%d+.%d+.%d+ | ') then
        rakBotIp = text:match('Nick %[[%w%W_]+%]  R%-IP %[%d+.%d+.%d+.%d+%]  IP | A%-IP %[{%w+}(%d+.%d+.%d+.%d+) | ')
        print('RakBot IP: ' .. rakBotIp)
    end
end

function isSpecialCommand(command)
    commandText = command['text']
    commandId = command['id']

    if commandText:find('>> sendmoney') then
        player, amount = commandText:match('>> sendmoney ([%w%_%d]+) (%d+)')
        sendInput('/abankmenu')
        newTask(sendDialogResponse, 300, 33, 1, 3, 'ok')
        newTask(sendDialogResponse, 300, 37, 1, -1, player)
        newTask(sendDialogResponse, 300, 41, 1, -1, amount)
        API.acceptCommand(commandId, bankTransfer)
        bankTransfer = {}
        return true
    end

    if commandText:find('>> stats') then
        sendInput('/stats')
        return true
    end

    if commandText:find('>> checkoff') then
        player = commandText:match('>> checkoff ([%w%_%d]+)')
        sendInput('/checkoff ' .. player)
        wait(1000)
        API.acceptCommand(commandId, checkoff)
        checkoff = {}
        return true
    end

    if commandText:find('>> clearrakbot') then
        nickname, ip = commandText:match('>> clearrakbot ([%w%_%d]+) (%d+.%d+.%d+.%d+)')
        table.insert(rakBotClearQueue, {nickname, ip, commandId})
        API.acceptCommand(commandId, {
            ["message"] = "you are in queue",
            ["kicked"] = false
        })
        return true
    end

    return false
end

function clearRakBot()
    while true do
        if #rakBotClearQueue > 0 then
            local counter = 0
            for i = 1, #rakBotClearQueue do
                print(i, 'rakbot on:', rakBotClearQueue[i][1], rakBotClearQueue[i][2], rakBotClearQueue[i][3])
            end

            local player = table.remove(rakBotClearQueue)
            sendInput('/getip ' .. player[1])

            wait(1000)
            while rakBotIp ~= player[2] do
                counter = counter + 1
                if lastRakBotIp ~= rakBotIp then
                    sendInput('/banipoff ' .. rakBotIp .. ' rakbot')
                    sendInput('/skick ' .. player[1])
                end
                lastRakBotIp = rakBotIp
                print('Ban. Try # ' .. counter .. ' BotIP: [' .. rakBotIp .. '] UserIP: [' .. player[2] .. ']')

                if counter > 10 then
                    counter = 0
                    API.acceptCommand(player[3], {
                        ["message"] = "failed to kick",
                        ["kicked"] = false
                    })
                    break
                end

                if rakBotIp == player[2] then
                    API.acceptCommand(player[3], {
                        ["message"] = "successfully cleared account from rakbot ",
                        ["kicked"] = true
                    })
                    break
                end

                wait(5000)
            end
        end
        wait(1000)
    end
end

function polling()
    newTask(clearRakBot)
    while true do
        local commands = API.getCommands()
        for i = 1, #commands do
            if not isSpecialCommand(commands[i]) then
                sendInput(u8:decode(commands[i]['text']))
                response = {
                    ['status'] = 'ok',
                    ['message'] = "Command send"
                }
                API.acceptCommand(commands[i]['id'], response)
            end
            wait(1000)
        end
        wait(2000)
    end
end

function onRunCommand(command)
    if command:find('poll') then
        newTask(polling)
    end
end
