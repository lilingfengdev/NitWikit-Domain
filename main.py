import time

from core.hook import *
from core.issue import *
import core.backend as dns
from core.checker import *
from core.backend.base import DNS
from core.payload import init_payload

domain = {
    "mcfun.us.kg": dns.CloudFlare,
    "nitwikit.us.kg": dns.CloudFlare,
    "yizhan.us.kg": dns.CloudFlare,
    "playmc.imc.rip": dns.DnsPod,
    "mc.imc.rip": dns.DnsPod,
    "llf.myredirect.us": dns.ExitDNS,
    "mc.lookin.at": dns.ExitDNS,
    "mcfun.findhere.org": dns.ExitDNS,
    "mcfun.lookin.at": dns.ExitDNS,
    "nitwikit.myfw.us": dns.ExitDNS,
    "playmc.lookin.at": dns.ExitDNS,
    "playmc.myfw.us": dns.ExitDNS,
    "playmc.rr.nu": dns.ExitDNS,
    "yizhan.findhere.org": dns.ExitDNS,
    "yizhan.myfw.us": dns.ExitDNS,
    "yizhan.rr.nu": dns.ExitDNS,
    "int.linkpc.net": dns.ExitDNS,
    "mcpvp.com.mp": dns.ExitDNS,
    "playmc.cloud-ip.biz": dns.ExitDNS,
    "playmc.com.mp": dns.ExitDNS,
    "playmc.myredirect.us": dns.ExitDNS,
    "pvp.line.pm": dns.ExitDNS,
    "pvp.findhere.org": dns.ExitDNS,
    "mcpvp.rr.nu": dns.ExitDNS,
    "mc.isgre.at": dns.ExitDNS,
    "pvp.isgre.at": dns.ExitDNS,
    "xixi.isgre.at": dns.ExitDNS,
    "mcpvp.blogu.tc": dns.ExitDNS,
    "xixi.san.tc": dns.ExitDNS,
    "lilf.dev.tc": dns.ExitDNS,
}


def main():
    sys.excepthook = except_hook
    init_payload()
    issue.create_commit("欢迎使用笨蛋文档域名服务！现在正在为你检查,请稍后")
    try:
        check(domain.keys())
    except CheckError as e:
        issue.create_commit(f"检查错误:`{e.msg}`,请更正后重新申请")
        issue.close()
        exit()
    issue.create_commit("检查成功,开始创建DNS记录")
    manager: DNS = domain[Request.domain](Request.domain)
    manager.connect()
    manager.create_record(
        subdomain=Request.subdomain,
        record_type=Request.record_type,
        record_value=Request.record_target
    )
    manager.create_record(
        subdomain="_create." + Request.subdomain,
        record_type="TXT",
        record_value=f"{issue.owner()}:{time.time()}"
    )
    if Request.srv and not isinstance(manager, dns.ExitDNS):
        manager.create_record(
            subdomain="_minecraft._tcp." + Request.subdomain,
            record_type="SRV",
            record_value=f"5 0 {Request.record_target_port} {Request.record_target}"
        )

    issue.create_commit(f"成功创建,现在你可以通过`{Request.subdomain}.{Request.domain}`访问了(DNS更新需要一定时间)")
    issue.close()


if __name__ == '__main__':
    main()
