import ipaddress
import socket
from env import Request,disable_register

class CheckError(Exception):
    def __init__(self, msg):
        self.msg = msg
def check(domain_list):
    if not Request.subdomain.isalnum():
        raise CheckError("子域名只能包含数字和字母")
    try:
        socket.gethostbyname(f'{Request.subdomain}.{Request.domain}')
    except socket.gaierror:
        pass
    else:
        raise CheckError("域名已被使用")

    if Request.subdomain in disable_register:
        raise CheckError("子域名不允许注册")

    if not Request.record_target_port.isalpha():
        raise CheckError("端口必须为数字")

    if Request.srv:
        if not (65535 > int(Request.record_target_port) > 1):
            raise CheckError("端口必须在1~65535之间")

    if Request.record_type in ["A","AAAA"]:
        try:
            ip=ipaddress.ip_address(Request.record_target)
            assert ip.is_global
        except ValueError:
            raise CheckError("目标IP地址不合法")
        except AssertionError:
            raise CheckError("目标IP地址不是公网地址")
    elif Request.record_type == "CNAME":
        try:
            socket.gethostbyname(Request.record_target)
        except socket.gaierror:
            raise CheckError("目标域名不存在")
    else:
        raise CheckError("不合法的解析")

    if Request.domain not in domain_list:
        raise CheckError("主域名不存在")
