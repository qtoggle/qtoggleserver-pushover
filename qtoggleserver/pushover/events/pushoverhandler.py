
import aiohttp
import logging

from typing import List, Optional

from qtoggleserver.conf import settings
from qtoggleserver.core import events as core_events
from qtoggleserver.lib.templatenotifications import TemplateNotificationsHandler


logger = logging.getLogger(__name__)


class PushoverHandler(TemplateNotificationsHandler):
    BASE_URL = 'https://api.pushover.net/1'
    MESSAGES_ENDPOINT = '/messages.json'

    logger = logger

    def __init__(self, user_keys: List[str], api_key: str, **kwargs) -> None:
        self._user_keys: List[str] = user_keys
        self._api_key: str = api_key

        super().__init__(**kwargs)

    async def push_message(self, event: core_events.Event, title: str, body: Optional[str] = None, **kwargs) -> None:
        url = self.BASE_URL + self.MESSAGES_ENDPOINT
        data = {
            'title': title,
            'message': body or '&nbsp;',
            'html': 1,
            'token': self._api_key,
            'user': self._user_keys,
            'timestamp': int(event.get_timestamp())
        }

        if settings.public_url:
            data['url'] = settings.public_url
            data['url_title'] = 'Open App'

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                return await response.json()
