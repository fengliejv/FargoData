import os

DEFAULTS = {
    'DB_USERNAME': 'fargoinsight',
    'DB_PASSWORD': 'Fargowealth1357!',
    'DB_HOST': '4.242.20.9',
    'DB_PORT': 9536,
    'DB_DATABASE': 'DB_Insight',
    'DB_CHARSET': 'utf8',
    'OSS_KEY': 'w5qPjZeiOS5QHNERKHUb',
    'OSS_SECRET': 'cEK8wMyjhsrJ2rxuIHibOFLBjgUYQZjiFbu2ybYF',
    'OSS_HOST': '212.64.23.164:9527',
    'UBS_FILTER_RULES': {"The Disclaimer relevant to Global", "\nDisclosure Section", "\nDisclosure Appendix"},
    "APP_ENV": 'local',
    "SCHEDULER_ENABLED": 'false',
    "COS_SECRET_ID": '',
    "COS_SECRET_KEY": ''
}

def get_env(key):
    return os.environ.get(key, DEFAULTS.get(key))

class Config:
    ENV = get_env('APP_ENV')
    
    COS_SECRET_ID = get_env('COS_SECRET_ID')
    COS_SECRET_KEY = get_env('COS_SECRET_KEY')

    # 是否开启定时任务
    SCHEDULER_ENABLED = get_env('SCHEDULER_ENABLED')
    DB_USERNAME = get_env("DB_USERNAME")
    DB_PASSWORD = get_env("DB_PASSWORD")
    DB_HOST = get_env("DB_HOST")
    DB_PORT = get_env("DB_PORT")
    DB_DATABASE = get_env("DB_DATABASE")
    DB_CHARSET = get_env("DB_CHARSET")
    OSS_KEY = get_env("OSS_KEY")
    OSS_SECRET = get_env("OSS_SECRET")
    OSS_HOST = get_env("OSS_HOST")
    UBS_FILTER_RULERS = get_env("UBS_FILTER_RULES")

    if ENV == 'local':
        PATH = os.path.join(os.path.dirname(__file__), "temp/")
    else:
        PATH = f"/home/ibagents/files/research/"

    

