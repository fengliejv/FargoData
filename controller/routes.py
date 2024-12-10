from flask import current_app as app
from TimeJob.scrap.quartr_calendar_get import get_quartr_calendar
from TimeJob.scrap.get_zhongjin_research import get_zj_research
from TimeJob.scrap.get_sa_research import get_sa_research
from TimeJob.scrap.get_fargo_research import get_fargo_research
from TimeJob.scrap.get_gs_research import get_gs_research
from TimeJob.scrap.get_ubs_research import get_ubs_research
from TimeJob.scrap.get_jp_research import get_jp_research
from TimeJob.scrap.get_ms_research import get_ms_research
from TimeJob.parse.research_parse import research_parse
from TimeJob.embedding.research_embedding import sync_research_embedding
from TimeJob.content_generate.pre_handle_meta import pre_handle_meta
from TimeJob.sync_research_glide import sync_research_glide

@app.route('/')
def home():
    return "Hello, Flask with APScheduler!"

@app.route('/get_quartr_calendar')
def get_quartr():
    return get_quartr_calendar()

# Add manual trigger routes
@app.route('/trigger/quartr_calendar')
def trigger_quartr_calendar():
    get_quartr_calendar()
    return "Quartr calendar job triggered!"

@app.route('/trigger/zj_research')
def trigger_zj_research():
    get_zj_research()
    return "Zhongjin research job triggered!"

@app.route('/trigger/sa_research')
def trigger_sa_research():
    get_sa_research()
    return "SA research job triggered!"

@app.route('/trigger/fargo_research')
def trigger_fargo_research():
    get_fargo_research()
    return "Fargo research job triggered!"

@app.route('/trigger/gs_research')
def trigger_gs_research():
    get_gs_research()
    return "GS research job triggered!"

@app.route('/trigger/ubs_research')
def trigger_ubs_research():
    get_ubs_research()
    return "UBS research job triggered!"

@app.route('/trigger/jp_research')
def trigger_jp_research():
    get_jp_research()
    return "JP research job triggered!"

@app.route('/trigger/ms_research')
def trigger_ms_research():
    get_ms_research()
    return "MS research job triggered!"

@app.route('/trigger/research_parse')
def trigger_research_parse():
    research_parse()
    return "Research parse job triggered!"

@app.route('/trigger/sync_research_embedding')
def trigger_sync_research_embedding():
    sync_research_embedding()
    return "Research embedding job triggered!"

@app.route('/trigger/pre_handle_meta')
def trigger_pre_handle_meta():
    pre_handle_meta()
    return "Pre-handle meta job triggered!"

@app.route('/trigger/sync_research_glide')
def trigger_sync_research_glide():
    sync_research_glide()
    return "Sync research glide job triggered!"