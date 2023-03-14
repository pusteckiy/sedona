require('addon')

local sampev = require('samp.events')
local encoding = require('encoding')
local config = require('config')
local API = require('services.API')
local discord = require('services.discord')

function onConnect()
    discord.send('**[A]** RakBot connected to the server.')
end

function onDisconnect()
    discord.send('**[A]** RakBot disconnected from the server.')
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
end

function isSpecialCommand(command)
    if command:find('>> sendmoney') then
        player, amount = command:match('>> sendmoney ([%w%_%d]+) (%d+)')
        sendInput('/abankmenu')
        newTask(sendDialogResponse, 300, 33, 1, 3, 'ok')
        newTask(sendDialogResponse, 300, 37, 1, -1, player)
        newTask(sendDialogResponse, 300, 41, 1, -1, amount)
        return true
    end

    if command:find('>> stats') then
        sendInput('/stats')
    end

    return false
end

function polling()
    while true do
        commands = API.getCommands()
        for i = 1, #commands do
            if not isSpecialCommand(commands[i]['text']) then
                sendInput(u8:decode(commands[i]['text']))
            end
            API.acceptCommand(commands[i]['id'])
            wait(1000)
        end
        wait(5000)
    end
end

function onRunCommand(command)
    if command:find('poll') then
        newTask(polling)
    end
end
