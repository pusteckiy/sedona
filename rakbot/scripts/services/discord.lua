local requests = require 'requests'
local encoding = require 'encoding'

local config = require('config')

encoding.default = 'CP1251'
u8 = encoding.UTF8

local discord = {}

local headers = {
    ["Content-Type"] = "application/json"
}

function getDiscordData(message)
    return {
        ['content'] = u8:encode(message),
        ['username'] = u8:encode('RakSAMP')
    }
end

function discord.send(message)
    return requests.post(config.discord.hook, {
        headers = headers,
        data = getDiscordData(message)
    }).json()
end

return discord
