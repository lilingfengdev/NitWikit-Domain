from core.env import CloudFlareInfo
import cloudflare
from core.backend.base import DNS


class CloudFlare(DNS):
    def __init__(self, domain):
        self.domain = domain
        self.client: cloudflare.Cloudflare = None
        self.zone = None

    def connect(self):
        self.client = cloudflare.Cloudflare(
            api_token=CloudFlareInfo.api_token,
        )
        self.zone = self.client.zones.list(name=self.domain).to_dict()["result"][0]["id"]

    def create_record(self, subdomain, record_type, record_value):
        self.client.dns.records.create(
            zone_id=self.zone,
            name=subdomain,
            type=record_type,
            content=record_value,
            proxied=False,
        )

    def delete_record(self, subdomain):
        record_id = self.client.dns.records.list(
            zone_id=self.zone,
            name=subdomain,
        )
        self.client.dns.records.delete(record_id, zone_id=self.zone)
