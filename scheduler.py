from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import atexit

from TimeJob.sync_research_glide import sync_research_glide
from TimeJob.content_generate.pre_handle_meta import pre_handle_meta
from TimeJob.embedding.research_embedding import sync_research_embedding
from TimeJob.insight.sync_reseach import sync_research
from TimeJob.parse.research_parse import research_parse
from TimeJob.sa.sync_insight_sa_article import update
from TimeJob.scrap.get_fargo_research import get_fargo_research
from TimeJob.scrap.get_gs_research import get_gs_research
from TimeJob.scrap.get_jp_research import get_jp_research
from TimeJob.scrap.get_ms_research import get_ms_research
from TimeJob.scrap.get_sa_research import get_sa_research
from TimeJob.scrap.get_ubs_research import get_ubs_research
from TimeJob.scrap.get_zhongjin_research import get_zj_research
from TimeJob.scrap.quartr_calendar_get import get_quartr_calendar


def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.start()

    # 数据获取任务
    scheduler.add_job(
        func= get_quartr_calendar,
        trigger=CronTrigger(hour=3, minute=0),
        id='quartr_get_job',
        name='quartr_get_job',
        replace_existing=True)
    
    scheduler.add_job(
        func=get_zj_research,
        trigger=CronTrigger(hour='9,16', minute=0),
        id='zj_research_job',
        name='zj_research_job',
        replace_existing=True)

    scheduler.add_job(
        func= get_sa_research,
        trigger=CronTrigger(minute='0,15,30,45'),
        id='get_research_job',
        name='get_research_job',
        replace_existing=True)

    scheduler.add_job(
        func= get_fargo_research,
        trigger=CronTrigger(minute='0,15,30,45'),
        id='get_fargo_research',
        name='get_fargo_research',
        replace_existing=True)

    scheduler.add_job(
        func= get_gs_research,
        trigger=CronTrigger(minute='5,20,35,50'),
        id='get_gs_research_job',
        name='get_gs_research_job',
        replace_existing=True)


    scheduler.add_job(
        func= get_ubs_research,
        trigger=CronTrigger(minute='5,20,35,50'),
        id='get_ubs_research_job',
        name='get_ubs_research_job',
        replace_existing=True)
    
    scheduler.add_job(
        func= get_jp_research,
        trigger=CronTrigger(minute='5,20,35,50'),
        id='get_jp_research_job',
        name='get_jp_research_job',
        replace_existing=True)
    

    scheduler.add_job(
        func= get_ms_research,
        trigger=CronTrigger(minute='5,20,35,50'),
        id='get_ms_research_job',
        name='get_ms_research_job',
        replace_existing=True)
    

    # 研究报告解析任务
    scheduler.add_job(
        func=research_parse,
        trigger=CronTrigger(minute='*/3'),
        id='parse_research_job',
        name='parse_research_job',
        replace_existing=True)

    # 研究报告向量化任务
    scheduler.add_job(
        func=sync_research_embedding,
        trigger=CronTrigger(minute='*/2'),
        id='embedding_research_job',
        name='embedding_research_job',
        replace_existing=True)

    # 研究报告元数据处理任务
    scheduler.add_job(
        func=pre_handle_meta,
        trigger=CronTrigger(minute='*/7'),
        id='handle_meta_job',
        name='handle_meta_job',
        replace_existing=True)

    # 研究报告同步任务
    scheduler.add_job(
        func= sync_research_glide,
        trigger=CronTrigger(minute='*/5'),
        id='sync_research_glide',
        name='sync_research_glide',
        replace_existing=True)


    # 确保在应用退出时关闭调度器
    atexit.register(lambda: scheduler.shutdown())
    return scheduler
