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
    return response
end

function API.acceptCommand(command_id, response_json)
    return requests.put(config.api.url .. 'rak-bot/command/' .. command_id, {
        headers = headers,
        data = {
            ['json'] = response_json
        }
    }).json()
end

function API.serverConnect(status)
    return requests.put(config.api.url .. 'rak-bot/status', {
        headers = headers,
        data = {
            ['value'] = status
        }
    })
end

return API
