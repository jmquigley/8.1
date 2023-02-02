__all__ = ["IgnitionGateway"]

from com.inductiveautomation.ignition.gateway.tags.model import GatewayTagManager


class Gateway(object):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IgnitionGateway, cls).__new__(cls)

        return cls._instance

    def get(self):
        return self._instance

    def getTagManager(self):
        return GatewayTagManager()


IgnitionGateway = Gateway()
