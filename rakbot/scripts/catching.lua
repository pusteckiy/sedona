require('addon')

local sampev = require('samp.events')
local config = require('config')
local discord = require('services.discord')

local tempNick, tempCar, tempSalonType = '', '', ''
local searchSalonCatchTime = false

function sampev.onServerMessage(color, text)
    if tonumber(os.date('%M')) < 10 then
        if text:find('[%w_]+ %[%d+%] ����� [�-�]+ ID: %d+ �� ���%. ���� �� [%d%.]+ ms! %(old%)') then
            nick, propertyType, propertyId, time = text:match(
                '([%w_]+) %[%d+%] ����� ([�-�]+) ID: (%d+) �� ���%. ���� �� ([%d%.]+) ms! %(old%)')
            if tonumber(time) < 2 then
                message = os.date("%Y-%m-%d %T") .. ' ' .. nick .. ' ������ ' .. propertyType .. ' �' ..
                              propertyId .. ' �� ' .. time .. ' ���. � ��� ������� � ��������'
                sendInput('/jailoff ' .. nick .. ' 3000 ���� ' .. propertyType .. ' �' .. propertyId .. ' [' ..
                              time .. ']')
                discord.send(message)
            end
        end
    end

    if text:find(
        '%[A%] [%w_]+%[%d+%] ����� ��������� �� ���� %([%w-]+%), ����: %$%w+, ���������: [%w�-��-�]+%.') then
        tempNick, tempCar, tempSalonType = text:match(
            '%[A%] ([%w_]+)%[%d+%] ����� ��������� �� ���� %(([%w-]+)%), ����: %$%w+, ���������: ([%w�-��-�]+)%.')
        for i, salon in pairs(config.catching.salons) do
            if tempSalonType:find(salon) then
                searchSalonCatchTime = not searchSalonCatchTime
                break
            end
        end
    end

    if text:find('%[A%] ��������� ��� � ����: [%d%.]+ ms') and searchSalonCatchTime then
        searchSalonCatchTime = not searchSalonCatchTime
        wasInGosTime = text:match('%[A%] ��������� ��� � ����: ([%d%.]+) ms')
        if tonumber(wasInGosTime) < 300 then
            message = os.date("%Y-%m-%d %T") .. ' ' .. tempNick .. ' ������ ���� ' .. tempCar .. ' � ' ..
                          tempSalonType .. '. ��� � ���: ' .. wasInGosTime
            sendInput('/jailoff ' .. tempNick .. ' 3000 ���� ���� [' .. tempCar .. ']')
            discord.send(message)
        end
    end
end
