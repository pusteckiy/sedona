require('addon')

local sampev = require('samp.events')
local config = require('config')
local discord = require('services.discord')

local tempNick, tempCar, tempSalonType = '', '', ''
local searchSalonCatchTime = false

function sampev.onServerMessage(color, text)
    if tonumber(os.date('%M')) < 10 then
        if text:find('[%w_]+ %[%d+%] купил [а-я]+ ID: %d+ по гос%. цене за [%d%.]+ ms! %(old%)') then
            nick, propertyType, propertyId, time = text:match(
                '([%w_]+) %[%d+%] купил ([а-я]+) ID: (%d+) по гос%. цене за ([%d%.]+) ms! %(old%)')
            if tonumber(time) < 2 then
                message = os.date("%Y-%m-%d %T") .. ' ' .. nick .. ' поймал ' .. propertyType .. ' №' ..
                              propertyId .. ' за ' .. time .. ' сек. и был посажен в деморган'
                sendInput('/jailoff ' .. nick .. ' 3000 Опра ' .. propertyType .. ' №' .. propertyId .. ' [' ..
                              time .. ']')
                discord.send(message)
            end
        end
    end

    if text:find(
        '%[A%] [%w_]+%[%d+%] купил транспорт по госу %([%w-]+%), цена: %$%w+, автосалон: [%wа-яА-Я]+%.') then
        tempNick, tempCar, tempSalonType = text:match(
            '%[A%] ([%w_]+)%[%d+%] купил транспорт по госу %(([%w-]+)%), цена: %$%w+, автосалон: ([%wа-яА-Я]+)%.')
        for i, salon in pairs(config.catching.salons) do
            if tempSalonType:find(salon) then
                searchSalonCatchTime = not searchSalonCatchTime
                break
            end
        end
    end

    if text:find('%[A%] Транспорт был в госе: [%d%.]+ ms') and searchSalonCatchTime then
        searchSalonCatchTime = not searchSalonCatchTime
        wasInGosTime = text:match('%[A%] Транспорт был в госе: ([%d%.]+) ms')
        if tonumber(wasInGosTime) < 300 then
            message = os.date("%Y-%m-%d %T") .. ' ' .. tempNick .. ' поймал авто ' .. tempCar .. ' в ' ..
                          tempSalonType .. '. Был в гос: ' .. wasInGosTime
            sendInput('/jailoff ' .. tempNick .. ' 3000 Опра авто [' .. tempCar .. ']')
            discord.send(message)
        end
    end
end
