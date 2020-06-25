from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import logging
import requests

logger = logging.getLogger(__name__)

def register(cb):
	cb(wttr())


@loader.tds
class wttr(loader.Module):
	"""wttr.in"""
	strings = {
		"name": "wttr"
	}

	async def client_ready(self, client, db):
		self.client = client

	@loader.sudo
	async def wttr(self, message):
		""".wttr <city> for weather"""
		message.edit("<b>Weather by wttr.in</b>")
		city = utils.get_args(message)
		await message.edit("Getting weather...")
		r = requests.get("https://wttr.in/" + str(city) + "?format=%l:+%c+%t,+%w+%m")
		await message.edit(r.text)


