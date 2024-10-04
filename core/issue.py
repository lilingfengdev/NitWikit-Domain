import github
from core.env import GitHubInfo


class GithubIssue:
    def __init__(self):
        self.repo = github.Github(GitHubInfo.token).get_repo("lilingfengdev/NitWikit-Domain")
        self.issue = self.repo.get_issue(GitHubInfo.issue_number)
        self.issue.lock("不接受评论")

    def create_commit(self, body):
        self.issue.unlock()
        self.issue.create_comment(body)
        self.issue.lock("不接受评论")

    def close(self):
        self.issue.edit(state='closed')
        self.issue.lock("已完成")

    def owner(self):
        return self.issue.user


issue = GithubIssue()
