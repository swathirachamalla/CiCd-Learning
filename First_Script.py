from github import Github
from datetime import datetime
import pytz
g = Github("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")
repo = g.get_repo("swathirachamalla/CiCd-Learning")
Branch= repo.get_branch("Development")
sha =Branch.commit.sha  
commit = repo.get_commit(sha=sha)
start_time = commit.commit.author.date
end_time =datetime.now(pytz.timezone('GMT'))
print(start_time,end_time)
