import json

import requests
from core.backend.base import DNS
from core.env import ExitDNSInfo

class ExitDNS(DNS):
    def __init__(self, domain):
        self.domain = domain
        self.session = requests.Session()
        self.api="https://api.dnsexit.com/dns/"

    def create_record(self, subdomain, record_type, record_value):
        self.session.post(
            url=self.api,
            data=json.dumps({
                "apikey": ExitDNSInfo.api_token ,
                "domain": self.domain,
                "add": {
                    "type": record_type,
                    "name": subdomain,
                    "content": record_value,
                    "overwrite": True,
                    "ttl": 1480,
                }
            })
        )


    def connect(self):
        pass