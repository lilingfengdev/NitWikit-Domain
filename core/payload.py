from core.env import Request
import os
import json


def init_payload():
    payload = json.loads(os.environ.get("PAYLOAD"))
    print(payload)
    Request.subdomain = payload["子域名名称"]
    Request.domain = payload["主域名"]
    Request.record_type = payload["记录类型"]
    Request.record_target = payload["解析目标"]
    Request.record_target_port = payload["解析目标端口的端口(启用SRV必填)"]
    Request.srv = payload["创建 SRV"]["创建"]
