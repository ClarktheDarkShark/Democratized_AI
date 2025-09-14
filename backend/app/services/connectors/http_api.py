from .base import BaseConnector

class HTTPAPIConnector(BaseConnector):
    def test(self, config):
        url = config.get("url", "")
        return url.startswith("http")
