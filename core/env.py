import os
class CloudFlareInfo:
    api_token=os.environ.get("CLOUDFLARE_API_TOKEN"),
class DnsPodInfo:
    user_id=os.environ.get("DNSPOD_USER_ID"),
    user_token=os.environ.get("DNSPOD_USER_TOKEN"),

class FreeDNSInfo:
    email=os.environ.get("FREE_DNS_EMAIL"),
    password=os.environ.get("FREE_DNS_PASSWORD"),

class GitHubInfo:
    token=os.environ.get("GITHUB_TOKEN")
    issue_number=os.environ.get("GITHUB_ISSUE_NUMBER")

class Request:
    domain=None
    subdomain=None
    record_type=None
    record_target=None
    record_target_port=None
    srv:bool=None
