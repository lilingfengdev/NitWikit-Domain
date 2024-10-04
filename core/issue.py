import github
from core.env import GitHubInfo


class GithubIssue:
    def __init__(self):
        self.repo = github.Github(GitHubInfo.token).get_repo("lilingfengdev/NitWikit-Domain")
        self.issue = self.repo.get_issue(GitHubInfo.issue_number)
        self.issue.lock("too heated")

    def create_commit(self, body):
        self.issue.unlock()
        self.issue.create_comment(body)
        self.issue.lock("too heated")

    def close(self):
        self.issue.lock("resolved")
        self.issue.edit(state='closed')

    def owner(self):
        return self.issue.user


issue = GithubIssue()
