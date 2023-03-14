local requests = require 'requests'
local encoding = require 'encoding'

local config = require('config')

encoding.default = 'CP1251'
u8 = encoding.UTF8

local API = {}

local headers = {
    ['Authorization'] = 'Token ' .. config.api.token,
    ['Content-Type'] = 'application/json'
}

function API.getCommands()
    response = requests.get(config.api.url .. 'rak-bot/command', {
        headers = headers
    }).json()
    return response['commands']
end

function API.acceptCommand(command_id)
    return requests.patch(config.api.url .. 'rak-bot/command', {
        headers = headers,
        data = {
            ["id"] = command_id
        }
    }).json()
end

return API
