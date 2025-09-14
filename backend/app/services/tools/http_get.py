import requests

from .base import BaseTool

ALLOWED_DOMAINS = {"example.com"}

class HTTPGetTool(BaseTool):
    name = "http_get"

    def execute(self, args):
        url = args.get("url", "")
        if not any(url.startswith(f"http://{d}") or url.startswith(f"https://{d}") for d in ALLOWED_DOMAINS):
            return {"error": "domain_not_allowed"}
        resp = requests.get(url, timeout=5)
        return {"status": resp.status_code, "content": resp.text[:200]}
