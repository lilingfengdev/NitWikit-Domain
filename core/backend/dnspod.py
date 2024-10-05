from typing import Optional
import pydnspod
from core.env import *
from core.backend.base import DNS


class DnsPod(DNS):
    def __init__(self, domain):
        self.client: Optional[pydnspod.Connection] = None
        self.domain = domain

    def connect(self):
        self.client = pydnspod.connect(DnsPodInfo.user_id, DnsPodInfo.user_token)

    def create_record(self, subdomain, record_type, record_value):
        self.client.record.add(
            domain=self.domain,
            record_type=record_type,
            value=record_value,
            sub_domain=subdomain
        )

    def delete_record(self, subdomain):
        for record in self.client.record.record_id(self.domain, subdomain):
            self.client.record.remove(self.domain, record)
