"""Get weather data using OpenWeatherMap
Syntax: .weather <Location> """

import aiohttp
import io
import time
from datetime import tzinfo, datetime
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="wttr (.*)"))
async def _(event):
    if event.fwd_from:
        return
    sample_url = "https://wttr.in/{}?format=%l:+%c+%t,+%w+%m"
    # logger.info(sample_url)
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str))
        # logger.info(response_api_zero)
        response_api = await response_api_zero.read()
    await event.edit(response_api["message"])
    
