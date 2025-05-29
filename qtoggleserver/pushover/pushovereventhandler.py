import logging

import aiohttp

from qtoggleserver.conf import settings
from qtoggleserver.core import events as core_events
from qtoggleserver.lib.templatenotifications import TemplateNotificationsHandler


logger = logging.getLogger(__name__)


class PushoverEventHandler(TemplateNotificationsHandler):
    BASE_URL = "https://api.pushover.net/1"
    MESSAGES_ENDPOINT = "/messages.json"

    logger = logger

    def __init__(self, *, user_keys: list[str], api_key: str, sound: str | None = None, **kwargs) -> None:
        self._user_keys: list[str] = user_keys
        self._api_key: str = api_key
        self._sound: str | None = sound

        super().__init__(**kwargs)

    async def push_message(self, event: core_events.Event, title: str, body: str | None = None, **kwargs) -> None:
        url = self.BASE_URL + self.MESSAGES_ENDPOINT
        data = {
            "title": title,
            "message": body or "&nbsp;",
            "html": 1,
            "token": self._api_key,
            "user": self._user_keys,
            "timestamp": int(event.get_timestamp()),
        }
        if self._sound:
            data["sound"] = self._sound

        if settings.public_url:
            data["url"] = settings.public_url
            data["url_title"] = "Open App"

        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.post(url, data=data) as response:
                await response.json()

        self.debug("message pushed")
