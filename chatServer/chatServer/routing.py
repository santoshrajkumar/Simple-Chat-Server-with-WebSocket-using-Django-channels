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