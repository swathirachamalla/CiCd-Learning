from github import Github
from datetime import datetime,timedelta
import os
import pytz
print("Executing First script")
g = Github("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")
repo = g.get_repo("swathirachamalla/CiCd-Learning")
Branch= repo.get_branch("Development")
sha =Branch.commit.sha  
commit = repo.get_commit(sha=sha)
start_time = commit.commit.author.date
end_time =datetime.now(pytz.timezone('GMT'))
c = datetime(end_time.year,end_time.month,end_time.day,end_time.hour,end_time.minute,end_time.second)- datetime(start_time.year,start_time.month,start_time.day,start_time.hour,start_time.minute,start_time.second)
print("c")
if c > timedelta(minutes=5):
    print("Executing Script.sh")
    os.system("bash script.sh")
