
import aiohttp
import logging
import time

from qtoggleserver.lib.templatenotifications import TemplateNotificationsHandler


logger = logging.getLogger(__name__)


class PushoverHandler(TemplateNotificationsHandler):
    BASE_URL = 'https://api.pushover.net/1'
    MESSAGES_ENDPOINT = '/messages.json'

    logger = logger

    def __init__(self, user_keys, api_key, **kwargs):
        self._user_keys = user_keys
        self._api_key = api_key

        super().__init__(**kwargs)

    async def push_message(self, event, title, body, **kwargs):
        url = self.BASE_URL + self.MESSAGES_ENDPOINT
        data = {
            'title': title,
            'message': body or '&nbsp;',
            'html': 1,
            'token': self._api_key,
            'user': self._user_keys,
            'timestamp': int(event.get_timestamp())
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                return await response.json()
