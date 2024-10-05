import os

disable_register = [
    "dnspodcheck",
    "www",
    "yizhan",
    "nitwikit",
    "lezi",
    "llf",
    "lilingfeng",
    "official",
    "fuckccf",
    "home",
    "china",
    "blog",
    "page",
]

class DnsPodInfo:
    user_id = os.environ.get("DNSPOD_USER_ID"),
    user_token = os.environ.get("DNSPOD_USER_TOKEN"),


class ExitDNSInfo:
    api_token = os.environ.get("EXITDNS_API_TOKEN"),


class GitHubInfo:
    token = os.environ.get("GITHUB_TOKEN")
    issue_number = int(os.environ.get("GITHUB_ISSUE_NUMBER"))


class Request:
    domain = None
    subdomain = None
    record_type = None
    record_target = None
    record_target_port = None
    srv: bool = None
