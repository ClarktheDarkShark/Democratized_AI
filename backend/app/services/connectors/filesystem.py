import os
from .base import BaseConnector

class FilesystemConnector(BaseConnector):
    def test(self, config):
        path = config.get("path", ".")
        return os.path.exists(path)
