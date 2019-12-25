### About

This is an addon for [qToggleServer](https://github.com/qtoggle/qtoggleserver).

It provides push notifications for qToggleServer via [Pushover](https://pushover.net/).


### Install

Install using pip:

    pip install qtoggleserver-pushover


### Usage

You'll need to register your account on [Pushover](https://pushover.net/), if you haven't done it yet. On their home
page, you'll see your *User Key*; copy it and use it in the configuration below. You can add more than one user key, if
you plan to send notifications to multiple users.

Then, you'll need a registered Pushover application (you can register one [here](https://pushover.net/apps/build)).
Copy the API key and use it in the configuration below:


##### `qtoggleserver.conf:`
``` javascript
...
event_handlers = [
    ...
    {
        driver = "qtoggleserver.pushover.events.PushoverHandler"
        user_keys = ["r7zxs1nj20w86bghyub5div8jyzyiw"]
        api_key = "nwn1cmgc9m6sjhrv1o4roebpb31b5i"
        ...
    }
    ...
]
...
```

For further customization, see
[Template Notifications](https://github.com/qtoggle/qtoggleserver/wiki/Template-Notifications)
