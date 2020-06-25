import request
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
    r = requests.get(sample_url.format(input_str))
    await event.edit(r.text["message"])
    
