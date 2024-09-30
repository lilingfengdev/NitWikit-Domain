
from core.env import *
from core.issue import *
from core.checker import *
from core.backend.base import DNS
from core.payload import init_payload

domain={
    "mcfun.us.kg":dns.CloudFlare,
    "nitwikit.us.kg":dns.CloudFlare,
    "yizhan.us.kg":dns.CloudFlare,
    "playmc.imc.rip":dns.DnsPod,
    "mc.imc.rip":dns.DnsPod,
    "llf.myredirect.us":dns.FreeDNS,
    "mc.lookin.at":dns.FreeDNS,
    "mcfun.findhere.org":dns.FreeDNS,
    "mcfun.lookin.at":dns.FreeDNS,
    "nitwikit.myfw.us":dns.FreeDNS,
    "playmc.lookin.at":dns.FreeDNS,
    "playmc.myfw.us":dns.FreeDNS,
    "playmc.rr.nu":dns.FreeDNS,
    "yizhan.findhere.org":dns.FreeDNS,
    "yizhan.myfw.us":dns.FreeDNS,
    "yizhan.rr.nu":dns.FreeDNS,
}

def main():
    init_payload()
    try:
        check(domain.keys())
    except CheckError as e:
        issue.create_commit(e.msg)
        issue.close()
        exit()

    manager:DNS=domain[Request.domain](Request.domain)
    manager.create_record(
        subdomain=Request.subdomain,
        record_type=Request.record_type,
        record_value=Request.record_target
    )
    manager.create_record(
        subdomain="_create."+Request.subdomain,
        record_type="TXT",
        record_value=issue.owner()
    )
    if Request.srv:
        manager.create_record(
            subdomain="_minecraft._tcp."+Request.subdomain,
            record_type="SRV",
            record_value=f"5 0 {Request.record_target_port} {Request.record_target}"
        )

    issue.create_commit(f"成功创建,现在你可以通过`{Request.subdomain}.{Request.domain}`访问了(DNS更新需要一定时间)")
    issue.close()

if __name__ == '__main__':
    main()



