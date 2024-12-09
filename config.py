import os


class Config:
    env = os.getenv('APP_ENV', 'development')

    if env == 'local':
        PATH = os.path.join(os.path.dirname(__file__), "research")
    else:
        PATH = f"/home/ibagents/files/research/"
    
    COS_SECRET_ID = os.getenv('COS_SECRET_ID', '')
    COS_SECRET_KEY = os.getenv('COS_SECRET_KEY', '')
