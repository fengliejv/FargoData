import os
import sys
#
# sys.path = ['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload',
#             '/home/ibagents/.virtualenvs/pythonProject1/lib/python3.10/site-packages',
#             '/home/ibagents/.local/lib/python3.10/site-packages', '/usr/local/lib/python3.10/dist-packages',
#             '/usr/lib/python3/dist-packages']
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from TimeJob.insight.sync_reseach import sync_research
from TimeJob.sa.sync_insight_sa_article import update

# if __name__ == '__main__':
#     sync_research()
#     update()

def sync_research_glide():
    sync_research()
    update()
