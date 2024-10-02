import sys
from core.issue import issue
def except_hook(t,v,tb):
    issue.create_commit(f"机器人出现错误！请联系管理员解决")
    issue.close()
