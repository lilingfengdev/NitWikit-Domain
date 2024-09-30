import ipaddress
import socket
from env import Request
class CheckError(Exception):
    pass
def check():
    if not Request.subdomain.isalnum():
        raise CheckError("子域名只能包含数字和字母")
    try:
        socket.gethostbyname(f'{Request.subdomain}.{Request.domain}')
    except socket.gaierror:
        pass
    else:
        raise CheckError("域名已被使用")

    if not Request.record_target_port.isalpha():
        raise CheckError("端口必须为数字")

    if not (65535 > int(Request.record_target_port) > 1):
        raise CheckError("端口必须在1~65535之间")

    try:
        ip=ipaddress.ip_address(Request.record_target)
        assert ip.is_global
    except (ValueError,AssertionError):
        raise CheckError("目标IP地址不合法")
