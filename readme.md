# Simple Chat Server with Django channels implementing websockets ⚡️ 

> This is the same project as depicted in  [<b>channels.readthedoc.io</b>](https://channels.readthedocs.io/en/latest/tutorial/part_2.html)
> However I have encountered few errors. For any new user this errors may be troublesome. That's why this repo is updated with the errors fixed.

## Fix 1:
* Use the follwoing snippet in the project/routing.py file instead of the code mentioned in [<b>channels.readthedoc.io</b>](https://channels.readthedocs.io/en/latest/tutorial/part_2.html)
```python
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat import routing

application = ProtocolTypeRouter({
  'websocket': AuthMiddlewareStack(
    URLRouter(
      routing.websocket_urlpatterns
    )
  ),
})
```

## Fix 2: Redis ERR unknown command 'BZPOPMIN' (for Windows users):
* You may have installed redis 3.2.100 from <b>MicrosoftArchive Redis</b>](https://github.com/microsoftarchive/redis/releases). But this gave me the above mentioned error.
To fix that, download redis 5.0.9 from <b>tporadowski/redis</b>](https://github.com/tporadowski/redis/releases). Run this server, and you'll be good.

Please give your feedback if found useful at: https://smrcontact.herokuapp.com


