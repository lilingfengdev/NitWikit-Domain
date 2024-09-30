import re
from core.env import FreeDNSInfo
import requests
from core.backend.base import DNS
class FreeDNS(DNS):
    def __init__(self,domain):
        self.headers = {
            "Host": "freedns.afraid.org",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.domain = domain
        self.dns_cookies = None
        self.domain_id = None
    def connect(self):
        username=FreeDNSInfo.email
        password=FreeDNSInfo.password
        headers = {
            "Accept-Language": "en-US"
        }
        url = "https://freedns.afraid.org/zc.php?step=2"
        payload = {
            'username': username,
            'password': password,
            'submit': 'Login',
            'action': 'auth'
        }
        attempts = 2
        while attempts >= 0:
            self.session.post(url, headers=headers, data=payload)
            self.dns_cookies = self.session.cookies.get('dns_cookie')
            htmlpage = self.session.get("https://freedns.afraid.org/subdomain/").text
            domain_id = re.search(fr'<td>{self.domain}</td>(.*?)</a>',htmlpage,flags=re.S)
            if domain_id:
                domain_id = re.search(r'edit\.php\?edit_domain_id=([0-9a-zA-Z]*)', domain_id.group(0))
                self.domain_id = domain_id.group(0)
                return
            attempts-=1
        raise Exception("无法连接到 FreeDNS")
    def create_record(self, subdomain, record_type, record_value):
        url = "https://freedns.afraid.org/subdomain/save.php?step=2"

        data = {
            "type": record_type,
            "domain_id": self.domain_id,
            "subdomain": subdomain,
            "address": f'"{record_value}"',
            "send": "Save!"
        }
        self.session.post(url, data=data)

